import drilldown
import imagedata

if __name__ == "__main__":
    folder = input('Provide the folder path: ') # Getting the path of the folder to drill down into
    images = drilldown.drilldown(folder) # Getting the list of images in the folder and all sub-folders
    print('images: ', images)
    metadata = []
    i = 0 # testing
    size = images.__len__() # testing
    for image in images:
        print(str(i), '\\', size) #testing
        i+=1 #testing
        metadata.append(imagedata.get_image_metadata(image)) # Fetching metadata for each image for later comparisons

    print("meta: ", metadata)