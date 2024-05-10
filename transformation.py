import cv2

def rotate_image(input_image_path, degrees = 90):
    try:
        # Read the image
        img = cv2.imread(input_image_path)

        # Get the image dimensions
        height, width = img.shape[:2]

        # Calculate the rotation matrix
        rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), degrees, 1)

        # Apply the rotation to the image
        rotated_img = cv2.warpAffine(img, rotation_matrix, (width, height))

        return rotate_image
    except Exception as e:
        print(f"An error occurred: {e}")

def resize(image, height, width):
    try:
        # Read the image
        img = cv2.imread(image)

        # Resize the image
        new_height = 360
        new_width = int(width * (new_height / height))
        resized_img = cv2.resize(img, (new_width, new_height)) #Convert the image to a 360x480 image

        # Save the resized image
        return id(resized_img)
    
    except Exception as e:
        print(f"An error occurred: {e}")