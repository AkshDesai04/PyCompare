import threading
import os
import numpy as np
import cv2

def comp():
    Img0 = cv2.imread("C:\\Users\\akshd\\Pictures\\test\\panorama-3725448.bmp")
    Img1 = cv2.imread("C:\\Users\\akshd\\Pictures\\test\\panorama-3725448.bmp")

    if Img0.shape == Img1.shape:
        difference = cv2.subtract(Img0, Img1)
        b, g, r = cv2.split(difference)

        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            print("Images EQUAL")
        else:
            print("Images NOT equal")
    else:
        print("Images NOT equal")

for i in range(10):
    comp()