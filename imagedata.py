import cv2
import os
import exifread

default_keys = ['File Size  (bytes)', 'Image Make', 'Image Model', 'Image Software', 'Image DateTime', 'GPS GPSLatitude', 'GPS GPSLongitude', 'EXIF ExposureTime', 'EXIF ISOSpeedRatings', 'EXIF ShutterSpeedValue', 'EXIF FocalLength', 'EXIF SubSecTime']

def get_image_metadata(image_path):
    try:
        # Read the image using OpenCV
        img = cv2.imread(image_path)

        # Get image dimensions
        height, width, channels = img.shape

        # Get image file size
        file_size_bytes = os.path.getsize(image_path)

        # Get image file format
        file_format = image_path.split('.')[-1]

        metadata = {
            "Width": width,
            "Height": height,
            "Channels": channels,
            "File Size (bytes)": file_size_bytes,
            "File Format": file_format
        }

        # Extract EXIF data if available (for JPEG images)
        if file_format.lower() == 'jpg' or file_format.lower() == 'jpeg':
            with open(image_path, 'rb') as f:
                tags = exifread.process_file(f)
                for tag in tags.keys():
                    metadata[str(tag)] = str(tags[tag])

        return metadata
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
def compare_metadata(metadata, keys = default_keys):
    seen_pairs = set()
    for sublist in metadata:
        pair = tuple(sublist.get(key) for key in keys)
        if pair in seen_pairs:
            return True
        seen_pairs.add(pair)
    return False