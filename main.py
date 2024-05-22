import sys
import cv2
import drilldown
import imagedata
from compare import compare_images_cuda
import transformation
from pprint import pprint
import defaults
import orchestrator
from memory_profiler import profile
import psutil
import threading
import time

def print_system_stats():
    while True:
        # CPU usage
        cpu_usage = psutil.cpu_percent(interval=1)
        
        # RAM usage
        memory_info = psutil.virtual_memory()
        ram_usage = memory_info.percent
        
        # Disk usage
        disk_info = psutil.disk_usage('/')
        disk_usage = disk_info.percent
        
        # Print the system stats
        print(f"CPU Usage: {cpu_usage}%")
        print(f"RAM Usage: {ram_usage}%")
        print(f"Disk Usage: {disk_usage}%")
        print('-' * 20)
        
        # Wait for 5 seconds
        time.sleep(5)

def main():
    metadata = []
    duplicates = []
    proxy_images = []

    # folder = input('Provide the folder path: ') # Getting the path of the folder to drill down into
    folder = "./" #temp
    images = drilldown.drilldown(folder) # Getting the list of images in the folder and all sub-folders

    # pprint(f"images: {[str(path_object) for path_object in images]}") # more readable than the simple print 
    for image in images:
        print('image ingest')
        img = cv2.imread(image)
        metadata.append(imagedata.get_image_metadata(image, img)) # Fetching metadata for each image for later comparisons
        proxy_images.append(transformation.resize(img)) # Creating Proxy images and storing in memory

    path = ''
    i = 0
    for img_write in proxy_images:
        print('writing i')
        cv2.imwrite("proxy_file-" + path + str(i) + '.jpg', img_write)
        i += 1

    print('proxy_images size: ', str(sys.getsizeof(proxy_images)))
    print('metadata size: ', str(sys.getsizeof(metadata)))

    try:
        for i in range(len(metadata)):
            for j in range(i + 1, len(metadata)):
                print(f"Comparing {images[i]} with {images[j]}")
                if metadata[i] == metadata[j]:
                    duplicates.append(images[j])
                else:
                    if compare_images_cuda(proxy_images[i], proxy_images[j]):
                        if compare_images_cuda(cv2.imread(images[i]), cv2.imread(images[j])):
                            duplicates.append(images[j])

        for duplicate in duplicates:
            # orchestrator.duplicate_management(duplicate, images, metadata, proxy_images, defaults.PRINT_ONLY)
            pass #TODO: Uncomment and remove pass while testing and in production. Commented function call to avoid deleting files.
    except Exception as e:
        print('Error: ', e)
        pass

    #Holding output for Testing
    input('Done and waiting to die. Press Enter to kill.')
    #Holding output for Testing

if __name__ == "__main__":
    # Start the system stats monitoring in a separate thread
    stats_thread = threading.Thread(target=print_system_stats)
    stats_thread.daemon = True
    stats_thread.start()
    
    main()
