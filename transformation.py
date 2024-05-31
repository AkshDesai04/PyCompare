import cv2


new_dimension = 100

def rotate_image(input_image, degrees = 90):
    try:
        rotate_image = cv2.rotate(input_image, cv2.ROTATE_90_CLOCKWISE)

        return rotate_image
    except Exception as e:
        print(f"An error occurred: {e}")

def resize(img, height = new_dimension, width = new_dimension):
    try:
        # Resize the image
        resized_img = cv2.resize(img, (width, height)) #Convert the image to a 360x360 image

        # Save the resized image
        return resized_img
    
    except Exception as e:
        print(f"An error occurred: {e}")