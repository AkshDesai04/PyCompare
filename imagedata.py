import cv2
import os
import exifread

def get_image_metadata(image_path):
    try:
        # Read the image using OpenCV
        print("Starting read")
        img = cv2.imread(image_path)
        print("Everything else")

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