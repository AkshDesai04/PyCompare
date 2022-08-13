import cv2
import numpy as np
import threading

def testing(number):
    for i in range(0, 1): #set to 48 while testing
        print("called")
        Img0 = cv2.imread("muslim-7059888.png")
        Img1 = cv2.imread("muslim-7059888.png")

        if Img0.shape == Img1.shape:
            difference = cv2.subtract(Img0, Img1)
            b, g, r = cv2.split(difference)

            if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
                print(number + "The images are completely Equal")
            else:
                print(number + "The images are not Equal")
        else: 
            print(number + "The images are not Equal")

print("called")
t1 = threading.Thread(target=testing, args=("1",))
t2 = threading.Thread(target=testing, args=("2",))
t3 = threading.Thread(target=testing, args=("3",))
t4 = threading.Thread(target=testing, args=("4",))
t5 = threading.Thread(target=testing, args=("5",))
t6 = threading.Thread(target=testing, args=("6",))
t7 = threading.Thread(target=testing, args=("7",))
t8 = threading.Thread(target=testing, args=("8",))
print("called")
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
print("called")
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
print("called")
print("Byeeeeeee")



# for i in range(0, 48):
#     testing(f"{i} ")