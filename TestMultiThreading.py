# import threading

# def PrintThis(n, x):
#     print(x, n)

# nums = []
# for i in range(1, 11):
#     nums.append(i)

# Len = 10

# # PrintThis(nums[1])
# # print(nums)

# # t1 = threading.Thread(target=PrintThis, args=(nums[1]))

# x = 0

# # for i in range(x ,Len):
# #     t1 = threading.Thread(target=PrintThis, args=(nums[x], 0),)
# #     x+=1
# #     t2 = threading.Thread(target=PrintThis, args=(nums[x], 1),)
# #     x+=1
# #     t3 = threading.Thread(target=PrintThis, args=(nums[x], 2),)
# #     x+=1
# #     t1.start()
# #     t2.start()
# #     t3.start()
# #    THIS THING WORKS!!!!!!!!!!

# size = 6

# for i in range(1, size):
#     for j in range(i+1, size):
#         print(i, j)



























import threading





inp = int(input("Enter length")) + 1

nums = []
for i in range(1, inp):
    nums.append(i)

len = len(nums)

def testing(n, a, b):
    print(a, "\t", b, "\tThread number: ", n)
    

print(nums)

for i in range(len):
    for j in range(i+1, len):
        try:
            t1 = threading.Thread(target=testing, args=("1", nums[i], nums[j]),)
            t1.start()
            j+=1
            t2 = threading.Thread(target=testing, args=("2", nums[i], nums[j]),)
            t2.start()
            j+=1
            t3 = threading.Thread(target=testing, args=("3", nums[i], nums[j]),)
            t3.start()
            j+=1
            t4 = threading.Thread(target=testing, args=("4", nums[i], nums[j]),)
            t4.start()
            j+=1
            t5 = threading.Thread(target=testing, args=("5", nums[i], nums[j]),)
            t5.start()
            j+=1
            t6 = threading.Thread(target=testing, args=("6", nums[i], nums[j]),)
            t6.start()
            j+=1
            t7 = threading.Thread(target=testing, args=("7", nums[i], nums[j]),)
            t7.start()
            j+=1
            t8 = threading.Thread(target=testing, args=("8", nums[i], nums[j]),)
            t8.start()
            j+=1
        except IndexError:
            continue