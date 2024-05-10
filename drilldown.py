from pathlib import Path

def drilldown(targeted_directory, extensions = ['.bmp', '.dib', '.jpeg', '.jpg', '.jp2', '.png', '.pbm', '.pgm', '.ppm', '.sr', '.ras', '.tiff', '.tif', '.exr', '.jxr', '.pfm', '.pds', '.pfm', '.viff', '.xbm', '.xpm', '.dds', '.eis', '.mng', '.web', '.hei', '.hei', '.av']):
    image_files:list[str]= []
    folder_path:Path = Path(targeted_directory)
    
    for file_path in folder_path.glob('**/*'):
        if file_path.is_file() and file_path.suffix.lower() in extensions:
            raw_filename = u'{}'.format(file_path)
            image_files.append(raw_filename)