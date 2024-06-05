import os
import cv2
import json
import exifread
import traceback
import numpy as np
from typing import List
from scipy import fftpack
from dataclasses import dataclass, fields

@dataclass
class Metadata:
    width: int
    height: int
    channels: int
    size: int
    extension: str
    exiftags: dict
    filename: str
    filepath: str
    hash: 'ImageHash'

    def __eq__(self, other: 'Metadata'):
        if not isinstance(other, Metadata):
            return False
        # current_hash = self.calculate_hash()
        # other_hash = other.calculate_hash()
        # if current_hash and other_hash and current_hash == other_hash:
        #     return True
        return (self.hash - other.hash) < 0.01
    
    def calculate_hash(self):
        if len(self.exiftags.keys()) == 0:
            return ""
        return json.dumps({k: self.exiftags[k] for k in sorted(self.exiftags)}, default=str)

def _binary_array_to_hex(arr: np.ndarray[bool]):
    """
    internal function to make a hex string out of a binary array.
    """
    bit_string = ''.join(str(b) for b in 1 * arr.flatten())
    width = int(np.ceil(len(bit_string) / 4))
    return '{:0>{width}x}'.format(int(bit_string, 2), width=width)

def hex_to_hash(hexstr: str):
	"""
	Convert a stored hash (hex, as retrieved from str(Imagehash))
	back to a Imagehash object.

	Notes:
	1. This algorithm assumes all hashes are either
			bidimensional arrays with dimensions hash_size * hash_size,
			or onedimensional arrays with dimensions binbits * 14.
	2. This algorithm does not work for hash_size < 2.
	"""
	hash_size = int(np.sqrt(len(hexstr) * 4))
	# assert hash_size == numpy.sqrt(len(hexstr)*4)
	binary_array = '{:0>{width}b}'.format(int(hexstr, 16), width=hash_size * hash_size)
	bit_rows = [binary_array[i:i + hash_size] for i in range(0, len(binary_array), hash_size)]
	hash_array = np.array([[bool(int(d)) for d in row] for row in bit_rows])
	return hash_array

class IndividualHash:
    def __init__(self, hash_value: np.ndarray[bool]):
        
        if isinstance(hash_value, np.ndarray):
            self.__hash: np.ndarray[bool] = np.copy(hash_value)
        else:
            raise ValueError(f"Expected ndarray or str. Received {type(hash_value)=}, {hash_value=}")
    
    def __str__(self):
        return _binary_array_to_hex(self.hash.flatten())
    
    def __repr__(self):
        return repr(self.__hash)
    
    @property
    def hash(self):
        return self.__hash

    def __sub__(self, other: 'IndividualHash'):
        if not isinstance(other, IndividualHash):
            raise TypeError(f"Cannot subtract with {type(other)=}")
        if self.hash.size != other.hash.size:
            raise TypeError('ImageHashes must be of the same shape.', self.hash.shape, other.hash.shape)
        return np.count_nonzero(self.hash.flatten() != other.hash.flatten()) / self.hash.size
    
    def __eq__(self, other: 'IndividualHash'):
        if not isinstance(other, IndividualHash):
            return False
        return np.array_equal(self.hash.flatten(), other.hash.flatten())
    
    def __ne__(self, other: 'IndividualHash'):
        if not isinstance(other, IndividualHash):
            return False
        return not np.array_equal(self.hash.flatten(), other.hash.flatten())
    
    def __hash__(self):
        return sum([2**(i % 8) for i, v in enumerate(self.hash.flatten()) if v])
    
    def __len__(self):
        return self.hash.size
    
    @classmethod
    def from_str(cls, hash_str: str):
        return cls(hex_to_hash(hash_str))

class ImageHash:
    __VERSION__ = 1

    def __init__(self):
        self.__hashes = np.empty(4, np.ndarray)
    
    def __str__(self):
        if np.count_nonzero(self.__hashes) == 0:
            return str(None)
        # {version:6}{hash_len:6}{hashsxhashsxhashsxhashsx}
        return f"{self.__VERSION__:#0{6}x}{len(str(self.__hashes[-1])):#0{6}x}{''.join([str(hash_val) for hash_val in self.__hashes])}"
    
    def __repr__(self):
        return repr(self.__hashes)
    
    @property
    def hashes(self):
        return self.__hashes
    
    def add_hash(self, hash_value: IndividualHash):
        if np.count_nonzero(self.__hashes) > 0:
            if len(hash_value) != len(self.__hashes[-1]):
                raise ValueError(f"Cannot add different length hashes to same image hash. Expecting {len(self.__hashes[-1])=}, Recieved {len(hash_value)=}")
        if np.count_nonzero(self.__hashes) < 4:
            self.__hashes[np.count_nonzero(self.__hashes)-1] = hash_value
            return True
        else:
            return False
    
    def __sub__(self, other: 'ImageHash'):
        if not isinstance(other, ImageHash):
            raise TypeError(f"Cannot subtract with {type(other)=}")
        values: List[int] = []
        for current_hash_val in self.__hashes:
            for other_hash_val in other.hashes:
                values.append(current_hash_val - other_hash_val)
        if len(values) == 0:
            raise ValueError("No hashes to subtract")
        # print(f"{values=}")
        return min(values)
    
    def __eq__(self, other: 'ImageHash'):
        if not isinstance(other, ImageHash):
            return False
        for current_hash_val in self.__hashes:
            for other_hash_val in other.hashes:
                if current_hash_val == other_hash_val:
                    return True
        return False
    
    def __ne__(self, other: 'ImageHash'):
        if not isinstance(other, ImageHash):
            return False
        for current_hash_val in self.__hashes:
            for other_hash_val in other.hashes:
                if current_hash_val == other_hash_val:
                    return False
        return True
    
    def __hash__(self):
        return sum([hash(hash_val) * (2 ** (i % 4)) for i, hash_val in enumerate(self.hashes)])
    
    def __len__(self):
        return len(self.hashes)
    
    @classmethod
    def from_str(cls, hash_str: str):
        obj = cls()
        version = int(hash_str[:6], 16)
        if obj.__VERSION__ != version:
            raise ValueError(f"Hash version expected {obj.__VERSION__}, recieved {version}")
        hash_length = int(hash_str[6:12], 16)
        # print()
        # print("=========== Loading hash ===========")
        # print(f"{version=}")
        # print(f"{hash_length=}")
        # print("=========== Loading hash ===========")
        # print()
        hashes_string = hash_str[12:]
        for i in range(0, len(hashes_string), hash_length):
            obj.add_hash(IndividualHash.from_str(hashes_string[i:i+hash_length]))
        return obj

def process_image(image_path: str):
    """
    Process image, get a metadata and hash for comparison
    """
    
    if not os.path.exists(image_path) or not os.path.isfile(image_path):
        return None
    
    image = cv2.imread(image_path)

    filename, extension = os.path.splitext(image_path)

    metadata = Metadata(
        width=image.shape[0],
        height=image.shape[1],
        channels=image.shape[2],
        size=os.path.getsize(image_path),
        extension=extension,
        filename=filename,
        filepath=os.path.abspath(image_path),
        exiftags={},
        hash=get_image_hash(image)
    )

    try:
        with open(image_path, 'rb') as f:
            for tag, value in exifread.process_file(f).items():
                metadata.exiftags[tag] = value
    except:
        # TODO: Decide on what to do in exiftags parsing failure. Currently doing nothing
        print(traceback.format_exc())
    
    return metadata

def get_image_hash(image: cv2.typing.MatLike, hash_size: int = 8, highfreq_factor: int = 4):

    img_size = hash_size * highfreq_factor

    sample = cv2.resize(image, (img_size, img_size))
    sample = cv2.cvtColor(sample, cv2.COLOR_BGR2GRAY)

    image_hash = ImageHash()

    for _ in range(4):

        dct = fftpack.dct(fftpack.dct(np.asarray(sample), axis=0), axis=1)

        dctlowfreq = dct[:hash_size, :hash_size]

        med = np.median(dctlowfreq)
        
        diff = dctlowfreq > med

        image_hash.add_hash(IndividualHash(diff))

        sample = cv2.rotate(sample, cv2.ROTATE_90_CLOCKWISE)
    
    return image_hash

if __name__ == "__main__":
    import pympler.asizeof
    
    image_paths = [
        # "/home/grayhat/desktop/github/PyCompare/_sample_data/COMP/IMG20240201171712.jpg",
        # "/home/grayhat/desktop/github/PyCompare/_sample_data/COMP/IMG20240201171717.jpg",
        # "/home/grayhat/desktop/github/PyCompare/_sample_data/Sem 4.png",
        # "/home/grayhat/desktop/github/PyCompare/_sample_data/Sem 6.png"
        # "/home/grayhat/desktop/github/PyCompare/_sample_data/Code Clash Cutouts Upper and Lower Seperated.png",
        # "/home/grayhat/desktop/github/PyCompare/_sample_data/Code Clash Text Cutput.png"
        # "/home/grayhat/desktop/github/PyCompare/_sample_data/COMP/IMG20240201175245.jpg",
        # "/home/grayhat/desktop/github/PyCompare/_sample_data/COMP/IMG20240201175252.jpg"
        "/home/grayhat/desktop/github/PyCompare/_sample_data/proxy/13.jpg",
        "/home/grayhat/desktop/github/PyCompare/_sample_data/proxy/7.jpg",
        # "/home/grayhat/desktop/github/PyCompare/_sample_data/proxy/189.jpg",
        # "/home/grayhat/desktop/github/PyCompare/_sample_data/proxy/246.jpg"
    ]

    loaded_hash = None

    for image_path in image_paths:
        print(f"{image_path=}")
        im_meta = process_image(image_path)

        print(f"{im_meta.channels=}")
        print(f"{im_meta.width=}")
        print(f"{im_meta.height=}")
        print(f"{im_meta.size=}")
        print(f"{im_meta.extension=}")
        print()
        print(f"========= exiftags ==========")
        for key in im_meta.exiftags.keys():
            print(f"im_meta.exiftags[{key=}]={im_meta.exiftags[key]}")
        print(f"========= exiftags ==========")
        print()
        print(f"{str(im_meta.hash)=}")

        import pympler
        print(f"{pympler.asizeof.asizeof(im_meta.hash)=}")

        if not loaded_hash:
            loaded_hash = ImageHash.from_str(str(im_meta.hash))
        
        else:
            print(f"{loaded_hash==im_meta.hash=}")
            print(f"{loaded_hash - im_meta.hash=}")
        
        print()
        print('======================================================================================')
        print()