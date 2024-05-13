import cv2
import drilldown
import imagedata
import compare
import transformation
from pprint import pprint 

if __name__ == "__main__":
    metadata = []
    duplicates = []
    proxy_images = []

    folder = input('Provide the folder path: ') # Getting the path of the folder to drill down into
    images = drilldown.drilldown(folder) # Getting the list of images in the folder and all sub-folders

    # pprint(f"images: {[str(path_object) for path_object in images]}") # more readable than the simple print 
    for image in images:
        img = cv2.imread(image)
        metadata.append(imagedata.get_image_metadata(image, img)) # Fetching metadata for each image for later comparisons
        proxy_images.append(transformation.resize(img)) # Creating Proxy images and storing in memory

    for i in range(len(metadata)):
        for j in range(i+1, len(metadata)):
            print(f"Comparing {images[i]} with {images[j]}")
            if(metadata[i] == metadata[j]):
                duplicates.append(images[j])
            else:
                if compare(proxy_images[i], proxy_images[j]):
                    if compare(cv2.imread(images[i]), cv2.imread(images[j])):
                        duplicates.append(images[j])