import cv2
import numpy as np


def compare(image1, image2):
    return open(image1, "rb").read() == open(image2, "rb").read()

def compare_images_cuda(image1, image2):
    # Upload the images to the GPU
    gpu_img1 = cv2.cuda_GpuMat()
    gpu_img2 = cv2.cuda_GpuMat()
    
    gpu_img1.upload(image1)
    gpu_img2.upload(image2)

    # Use the cv2.cuda functions to process the images on the GPU
    # Compute the absolute difference between the images
    gpu_diff = cv2.cuda.absdiff(gpu_img1, gpu_img2)

    # Download the result from GPU to CPU
    diff = gpu_diff.download()

    # Convert the difference image to grayscale
    gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # Compute the sum of absolute differences
    sad = cv2.sumElems(gray_diff)[0]

    # Optionally normalize the SAD value
    norm_sad = sad / (image1.shape[0] * image2.shape[1])

    return norm_sad