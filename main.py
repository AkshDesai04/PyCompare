import json
from dataclasses import asdict
from pycompare import get_duplicates
from pycompare.process import ImageHash

if __name__ == "__main__":

    folder = input("Input Folder path: ")
    
    # duplicates = get_duplicates("_sample_data")
    duplicates = get_duplicates(folder)

    # hash1 = ImageHash.from_str("0x00010x0010d58f6b3c6aa22ad090fe2bc42f853ab480253e963f083f7bc5503e6c7a0f6e1c")
    # hash2 = ImageHash.from_str("0x00010x0010cb4a4acac8ea5b1bc9ab5556aa55a2d49ee01f609d630fb19c0100dce3fdf378")

    # print(hash1-hash2)

    with open("duplicated.json", "w+") as f:
        json.dump([[asdict(metadata) for metadata in group] for group in duplicates], f, default=str)

    # for group in duplicates:
    #     print([metadata.filepath for metadata in group])