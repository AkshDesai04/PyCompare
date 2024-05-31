import cv2
import numpy as np

def compare(image1, image2, is_proxy = True):
    # Check if the images have been loaded correctly
    if image1 is None or image2 is None:
        raise ValueError("One or both of the image paths are invalid.")
    
    if not is_proxy:
        # Check if the dimensions are the same
        if image1.shape != image2.shape:
            return False
    
    # Compare the images
    difference = cv2.absdiff(image1, image2)
    if np.count_nonzero(difference) == 0:
        return True
    else:
        return False