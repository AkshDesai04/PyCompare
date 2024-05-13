import drilldown
import imagedata
from pprint import pprint 

if __name__ == "__main__":
    folder = input('Provide the folder path: ') # Getting the path of the folder to drill down into
    images = drilldown.drilldown(folder) # Getting the list of images in the folder and all sub-folders
    pprint(f"images: {[str(path_object) for path_object in images]}") # more readable than the simple print 
    metadata = []
    for image in images:
        metadata.append(imagedata.get_image_metadata(image)) # Fetching metadata for each image for later comparisons

    # print("meta: ", metadata)
    print(metadata)
    
    for i in range(len(metadata)):
        for j in range(i+1, len(metadata)):
            print(f"Comparing {images[i]} with {images[j]}")