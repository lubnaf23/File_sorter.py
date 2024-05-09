import os

file_path = '/Users/name/Downloads/filename' #example use local path

print(file_path)

if os.path.isfile(file_path):
    os.remove(file_path)
    print("Removed!!")
else:
    print("FILE DOES NOT EXIST")
