import threading
import os
import numpy as np
import cv2

def testing(number, File0, File1):
    Img0 = cv2.imread(File0)
    Img1 = cv2.imread(File1)

    if Img0.shape == Img1.shape:
        difference = cv2.subtract(Img0, Img1)
        b, g, r = cv2.split(difference)

        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            print("Images EQUAL", number,  "\t\t\t\t\t", File0, File1,)
        else:
            print("Images NOT equal", number,  "\t\t", File0, File1,)
    else:
        print("Images NOT equal", number,  "\t\t", File0, File1,)

dir_path = 'C:\\Users\\akshd\\Pictures\\test'

FilesList = []

for path, subdirs, files in os.walk(dir_path):
    for name in files:
        FilesList.append(os.path.join(path, name))

FilesList.sort()
len = len(FilesList)

x = 0

for i in range(1, len):
    for j in range(i+1, len):
        print(i, j)
        #
        t1 = threading.Thread(target=testing, args=("1", FilesList[i], FilesList[j]),)
        j+=1
        t2 = threading.Thread(target=testing, args=("2", FilesList[i], FilesList[j]),)
        j+=1
        t3 = threading.Thread(target=testing, args=("3", FilesList[i], FilesList[j]),)
        j+=1
        t4 = threading.Thread(target=testing, args=("4", FilesList[i], FilesList[j]),)
        j+=1
        t5 = threading.Thread(target=testing, args=("5", FilesList[i], FilesList[j]),)
        j+=1
        t6 = threading.Thread(target=testing, args=("6", FilesList[i], FilesList[j]),)
        j+=1
        t7 = threading.Thread(target=testing, args=("7", FilesList[i], FilesList[j]),)
        j+=1
        t8 = threading.Thread(target=testing, args=("8", FilesList[i], FilesList[j]),)
        j+=1
        #








t1 = threading.Thread(target=testing, args=("1", FilesList0[i], FilesList1[j]),)
t2 = threading.Thread(target=testing, args=("2", FilesList0[i], FilesList1[j]),)
t3 = threading.Thread(target=testing, args=("3", FilesList0[i], FilesList1[j]),)
t4 = threading.Thread(target=testing, args=("4", FilesList0[i], FilesList1[j]),)
t5 = threading.Thread(target=testing, args=("5", FilesList0[i], FilesList1[j]),)
t6 = threading.Thread(target=testing, args=("6", FilesList0[i], FilesList1[j]),)
t7 = threading.Thread(target=testing, args=("7", FilesList0[i], FilesList1[j]),)
t8 = threading.Thread(target=testing, args=("8", FilesList0[i], FilesList1[j]),)
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()








#TODO: CHANGE ATTRIBUTES OF TESTING FUNCTION AND MAKE IT JUST THE NUMBER
#TODO: TESTING FUNCTION SHOULD PICK UP FILE DIR FROM THE 2-D ARRAY THAT GLOBAL.
#TODO: THE ONLY ARGUMENT SHOULD BE THE THREAD'S NUMBER SO, THE FUNCTION CAN DISTRIBUTE TASKS.
#TODO: If a file is known to be a duplicate, do not check it with any other ones later on
#TODO: Print a list of all original files at the end
#TODO: Code in a progress bar/number
#TODO: Use only a single list/array of files and compare each element with every element under/after it