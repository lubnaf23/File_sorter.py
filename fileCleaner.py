import os

file_path = '/Users/syedh/Downloads/Lab0 waveform.png'

print(file_path)

if os.path.isfile(file_path):
    os.remove(file_path)
    print("Removed!!")
else:
    print("FILE DOES NOT EXIST")