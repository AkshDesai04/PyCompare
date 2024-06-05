from tqdm import tqdm
from typing import List
from pycompare import drilldown
from pycompare.process import process_image, Metadata

def get_duplicates(folder_path: str):
    image_paths = drilldown.drilldown(folder_path)

    # Mapping with image hash and metadata
    similarity_groups: List[List[Metadata]] = []

    for image_path in tqdm(image_paths):
        metadata = process_image(image_path)

        if not metadata:
            # TODO: Think about what should happen in an ideal scenario. Currently skipping
            continue
        
        inserted = False

        for group in similarity_groups:
            for meta in group:
                if meta == metadata:
                    group.append(metadata)
                    inserted = True
                    break
            if inserted:
                break
        
        if not inserted:
            similarity_groups.append([metadata])
    
    return [group for group in similarity_groups if len(group) > 1]