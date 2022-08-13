import os

dir_path = 'C:\\Users\\akshd\\Pictures\\test'
FilesList0 = []
FilesList1 = []

for path, subdirs, files in os.walk(dir_path):
    for name in files:
        FilesList0.append(os.path.join(path, name))

FilesList0.sort()
FilesList1 = FilesList0.copy()
print(FilesList1)

len = len(FilesList0)

for i in range(len):
    if FilesList0[i] != FilesList1[i]:
        print("Lists are not the same")
    else:
        print("Ok")

for i in range(len):
    if FilesList0[10] != FilesList1[i]:
        print("Lists are not the same")
    else:
        print("Ok")