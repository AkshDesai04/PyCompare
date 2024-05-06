import cv2
import numpy as np


def compare(image1, image2):
    return open(image1, "rb").read() == open(image2, "rb").read()