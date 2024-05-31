import sys # testing
import cv2
import drilldown
import imagedata
from compare import compare
import transformation
from pprint import pprint 
import defaults
import orchestrator

if __name__ == "__main__":
    metadata = []
    duplicates = []
    proxy_images = []

    # folder = input('Provide the folder path: ') # Getting the path of the folder to drill down into
    folder = '.\\ignore\\' # Getting the path of the folder to drill down into
    images = drilldown.drilldown(folder) # Getting the list of images in the folder and all sub-folders

    # pprint(f"images: {[str(path_object) for path_object in images]}") # more readable than the simple print 
    for image in images:
        print('image ingest')
        img = cv2.imread(image)
        metadata.append(imagedata.get_image_metadata(image, img)) # Fetching metadata for each image for later comparisons

        # Creating Proxy images and storing in memory
        p_main = transformation.resize(img) # Main proxy
        p_r_l1 = transformation.rotate_image(p_main) # Proxy rotating left 1
        p_r_l2 = transformation.rotate_image(p_r_l1) # Proxy rotating left 2
        p_r_l3 = transformation.rotate_image(p_r_l2) # Proxy rotating left 3

        proxy_images.append(p_main)
        proxy_images.append(p_r_l1)
        proxy_images.append(p_r_l2)
        proxy_images.append(p_r_l3)

    path = ''
    i = 0
    for img_write in proxy_images:
        print(f'writing {i}')
        try:
            print(".\\ignore\\proxy\\proxy_file-" + path+str(i) + '.jpg')
            cv2.imwrite(".\\ignore\\proxy\\proxy_file-" + path+str(i) + '.jpg', img_write)
            print("Success")
        except Exception as e:
            print(e)
        i += 1

    print('proxy_images size: ', str(sys.getsizeof(proxy_images)))
    print('metadata size: ', str(sys.getsizeof(metadata)))

    for i in range(len(metadata)):
        for j in range(i+1, len(metadata)):
            print(f"Comparing {images[i]} with {images[j]}")
            # if(metadata[i] == metadata[j]):
            #     duplicates.append(images[j])
            # else:
            if compare(proxy_images[i], proxy_images[j]):
                print("True")
                # if compare(cv2.imread(images[i]), cv2.imread(images[j]), False):
                #     print("True\n\n\n")
                #     duplicates.append(images[j])
                # else:
                #     print("False\n\n\n")

    for duplicate in duplicates:
        # orchestrator.duplicate_management(duplicate, images, metadata, proxy_images, defaults.PRINT_ONLY)
        pass #TODO: Uncomment and remove pass while testing and in production. Commented function call to avoid deleting files.
                    

    #Holding output for Testing
    input('Done and waiting to die. Press Enter to kill.')
    #Holding output for Testing