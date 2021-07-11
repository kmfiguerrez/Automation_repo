from pathlib import Path
from pdfTest import dir_Name
import os
import shutil

# Get to the pdf files dir location.
os.chdir(Path.home() / 'Downloads' / 'Layouting' / 'To work on' / 'Programming Java')
# set the pdf files directory location to pdf_files_loc variable.
pdf_files_loc = Path.cwd() 

"""
loop through each file in the pdf files directory.
then create a directory with name set to d variable.
then move each file to its corresponding directory.
""" 
for file in pdf_files_loc.glob('*'):
    # Set the directory name to variable d.
    d = dir_Name(file.name)
    # Set the new directory location to dir_path variable.
    dir_path = pdf_files_loc / d
    # Create the directory with the name set to d variable above.
    dir_path.mkdir()
    # Move the current file in the created directory.
    shutil.move(file, dir_path)

    

 
    
    