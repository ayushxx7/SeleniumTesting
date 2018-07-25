### RENAME sample_excel_files folder to excel_files
import os
import shutil
from os import path

def rename_sample_excel():
	# make a duplicate of an existing file
    if path.exists("sample_excel_files"):
	# get the path to the file in the current directory
        src = path.realpath("sample_excel_files");
		
	# rename the original file
        os.rename("sample_excel_files","excel_files")
# import os
# print(os.listdir())

# abs_dir_path = os.path.abspath(__file__) # absolute file path
# req_path = abs_dir_path.rpartition('\\')
# sample_excel_folder = req_path[0] + 
# os.rename()


# LOGIN CREDENTIALS FILES MUST BE FILLED
# run check login status



# run multi acc lib functions

# run api lib functions seperately
