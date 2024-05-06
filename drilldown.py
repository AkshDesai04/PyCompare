import os

def drilldown(folder_path, extensions = {'.bmp', '.dib', '.jpeg', '.jpg', '.jp2', '.png', '.pbm', '.pgm', '.ppm', '.sr', '.ras', '.tiff', '.tif', '.exr', '.jxr', '.pfm', '.pds', '.pfm', '.viff', '.xbm', '.xpm', '.dds', '.eis', '.mng', '.web', '.hei', '.hei', '.av'}):
    image_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_extension = os.path.splitext(file)[1].lower()
            if file_extension in extensions:
                image_files.append(os.path.join(root, file))
    return image_files


folder = input('Provide the folder path: ') # Getting the path of the folder to drill down into
images = drilldown(folder) # Getting the list of images in the folder and all sub-folders
print(images)