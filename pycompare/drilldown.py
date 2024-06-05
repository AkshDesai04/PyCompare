from typing import List
from pycompare.defaults import IMAGE_EXTENSIONS
from pathlib import Path

def drilldown(targeted_directory: str, extensions: List[str] = IMAGE_EXTENSIONS):
    image_files:list[str]= []
    folder_path:Path = Path(targeted_directory)
    if not folder_path.exists():
        raise ValueError(f"Folder path {targeted_directory} does not exist.")
    for file_path in folder_path.glob('**/*'):
        if file_path.is_file() and file_path.suffix.lower() in extensions:
            raw_filename = u'{}'.format(file_path)
            image_files.append(raw_filename)
    return image_files