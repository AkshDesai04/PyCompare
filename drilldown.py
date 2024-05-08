import os

from pathlib import Path

def drilldown(folder_path, extensions={'.bmp', '.dib', '.jpeg', '.jpg', '.jp2', '.png', '.pbm', '.pgm', '.ppm', '.sr', '.ras', '.tiff', '.tif', '.exr', '.jxr', '.pfm', '.pds', '.pfm', '.viff', '.xbm', '.xpm', '.dds', '.eis', '.mng', '.web', '.hei', '.hei', '.av'}):
    image_files = []
    folder_path = Path(folder_path)
    
    for file_path in folder_path.glob('**/*'):
        if file_path.is_file() and file_path.suffix.lower() in extensions:
            image_files.append(file_path)
    
    return image_files

folder = input('Provide the folder path: ') # Getting the path of the folder to drill down into
images = drilldown(folder) # Getting the list of images in the folder and all sub-folders
print(images)