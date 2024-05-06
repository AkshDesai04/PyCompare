import os

def find_images(folder_path, extensions):
    image_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_extension = os.path.splitext(file)[1].lower()
            if file_extension in extensions:
                image_files.append(os.path.join(root, file))
    return image_files