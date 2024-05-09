# File Sorter
#### -Lubna Firdaus

It is a Python automation script that sorts local files. There are two files in this repository which perform different functions. Both of them use the ***'os'*** module to access local files. 

## File Cleaner

### Description
This Python script is designed to remove particular file from the local computer if it exists. It utilizes ***'os.remove()'*** function from the ***'os'*** module if the file exists.

### Requirements
* Python 3x
* ***'os'*** module

### Usage
1. Clone or download ***'fileCleaner.py'*** to your local computer.
2. Open it in an editor and change the ***'file_path'***.
3. Run the Python file in the terminal.
4. The script will check if the specified file exists at the provided path. If the file exists, it will be removed, and a confirmation message will be displayed. If the file does not exist, a message indicating that the file does not exist will be displayed.

### Note
1. Ensure that the ***'file_path'*** variable is accurately set to the path of the file you want to remove.
2. Exercise caution when using this script, as it will permanently delete the specified file if it exists.
