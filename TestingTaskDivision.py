import threading
import os
import numpy as np
import cv2

N_O_T_ = 8 # Number of threads

def testing(number = 0):
    # i = number
    ThreadTaskList = []
    for i in range(len(FinalFilesList)):
        ThreadTaskList.append(FinalFilesList[i])




    # Img0 = cv2.imread(File0)
    # Img1 = cv2.imread(File1)

    # if Img0.shape == Img1.shape:
    #     difference = cv2.subtract(Img0, Img1)
    #     b, g, r = cv2.split(difference)

    #     if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
    #         print("Images EQUAL", number,  "\t\t\t\t\t", File0, File1,)
    #     else:
    #         print("Images NOT equal", number,  "\t\t", File0, File1,)
    # else:
    #     print("Images NOT equal", number,  "\t\t", File0, File1,)

dir_path = 'C:\\Users\\akshd\\Pictures\\test'

x = 0

FilesList0 = []
FilesList1 = []

for path, subdirs, files in os.walk(dir_path):
    for name in files:
        FilesList0.append(os.path.join(path, name))

FilesList0.sort()
FilesList1 = FilesList0.copy()
len = len(FilesList0)

FinalFilesList = [[""]*2]

for i in range(len):
    for j in range(i+1, len):
        FinalFilesList.append([FilesList0[i], FilesList1[j]])

testing(0)


        # try:
        #     x = x + 1
        #     t1 = threading.Thread(target=testing, args=(1,)
        #     t2 = threading.Thread(target=testing, args=(2,)
        #     t3 = threading.Thread(target=testing, args=(3,)
        #     t4 = threading.Thread(target=testing, args=(4,)
        #     t5 = threading.Thread(target=testing, args=(5,)
        #     t6 = threading.Thread(target=testing, args=(6,)
        #     t7 = threading.Thread(target=testing, args=(7,)
        #     t8 = threading.Thread(target=testing, args=(8,)
        #     t1.start()
        #     t2.start()
        #     t3.start()
        #     t4.start()
        #     t5.start()
        #     t6.start()
        #     t7.start()
        #     t8.start()
        #     t1.join()
        #     t2.join()
        #     t3.join()
        #     t4.join()
        #     t5.join()
        #     t6.join()
        #     t7.join()
        #     t8.join()
        #     print(x, "/ 4005")
        # except:
        #     print("Non-Image File Maybe? Continuing with the rest\nFiles: ", FilesList0[i], "\n", FilesList1[j])