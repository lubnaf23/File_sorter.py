import os
import shutil #to move files

def file_mover():
#The folder we want to clean
#"C:\Users\syedh\Downloads"
#"C:\Users\syedh\OneDrive\Documents"
    cleaning_folder = '/Users/syedh/OneDrive/Documents/'

#folder to move the file types to
#"C:\Users\syedh\OneDrive\Pictures"
    new_folder = '/Users/syedh/OneDrive/Pictures/'

#iterating over the entire cleaning folder
    for filename in os.listdir(cleaning_folder):
    #is it a specific type of file?
        if filename.endswith('.jpg'):
        #existing path
            source_path = os.path.join(cleaning_folder, filename)
        #new path
            new_path = os.path.join(new_folder, filename)
        #moving it to the new folder
            shutil.move(source_path, new_path)
            print("Moved the file", source_path, " to ", new_path)
            print("ALL CLEAR!")
        
file_mover()