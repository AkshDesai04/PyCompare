import os

dir_path = "D:"
files = []

for path, subdirs, files in os.walk(dir_path):
    for name in files:
        files.append(os.path.join(path, name))
        print(os.path.join(path, name))

print(files)