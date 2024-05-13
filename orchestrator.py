import os

def duplicate_managment(i, image_paths, metadata, proxy_images, decision):
    #if decision = 0 then print the path of file on i'th index of the images list. After that remove the i'th index from the metadata list and proxy_images list.
    #if decision = 1 then copy the image from the path of file on i'th index of the images list to a given directory. After that remove the i'th index from the metadata list and proxy_images list.
    #if decision = 2 then delete the image from the path of file on i'th index of the images list. After that remove the i'th index from the metadata list and proxy_images list.
    if decision == 0:
        print(f"Duplicate found at: {image_paths[i]}")
    elif decision == 1:
        os.system(f"copy {image_paths[i]} C:\\Users\\akshd\\Pictures\\duplicates")
    elif decision == 2:
        os.system(f"del {image_paths[i]}")