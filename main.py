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

# Number of threads to use
threads_to_use = 4

def process_image(image, metadata, proxy_images, duplicates):
    img = cv2.imread(image)
    image_metadata = imagedata.get_image_metadata(image, img)
    metadata.append(image_metadata)
    proxy_images.append(transformation.resize(img))

    for i, metadata_i in enumerate(metadata[:-1]):
        if metadata_i == image_metadata:
            if compare_images_cuda(proxy_images[i], proxy_images[-1]):
                if compare_images_cuda(cv2.imread(images[i]), cv2.imread(images[-1])):
                    duplicates.append(images[-1])

def main():
    metadata = []
    duplicates = []
    proxy_images = []

    # folder = input('Provide the folder path: ') # Getting the path of the folder to drill down into
    folder = "./" #temp
    images = drilldown.drilldown(folder) # Getting the list of images in the folder and all sub-folders

    threads = []
    for image in images:
        thread = threading.Thread(target=process_image, args=(image, metadata, proxy_images, duplicates))
        thread.start()
        threads.append(thread)

        # Limit the number of concurrent threads
        if len(threads) >= threads_to_use:
            for t in threads:
                t.join()
            threads = []

    for t in threads:
        t.join()

    # Handle duplicate images here

    # Hold output for Testing
    input('Done and waiting to die. Press Enter to kill.')
    # Hold output for Testing

if __name__ == "__main__":
    main()