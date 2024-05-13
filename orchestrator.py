import os
import defaults


def duplicate_management(i, image_paths, metadata, proxy_images, decision = defaults.PRINT_ONLY, destination = ''):
    match decision:
        case defaults.PRINT_ONLY:
            print(f"Duplicate found at: {image_paths[i]}")
        case defaults.COPY_ONLY:
            os.move(image_paths[i], destination.join(image_paths[i].split('/')))
        case defaults.DELETE_ONLY:
            os.remove(image_paths[i])
        
    del image_paths[i]
    del metadata[i]
    del proxy_images[i]