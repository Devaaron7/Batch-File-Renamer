import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askopenfilenames, askdirectory
import time

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
#filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
#print(filename)


# Prompts user to select file(s) you want to batch rename. Then adds the paths to a list (target)
print("Select the files you want to rename")
time.sleep(2)
target = list(askopenfilenames())



# For loop that checks every files extension and adds them individually to a empty list (ext)
ext = []
ct = 1
for a in target:
    temp = ""    
    while True:
        if a[-ct] != ".":
            temp += a[-ct]
            ct += 1
        if a[-ct] == ".":
            temp += a[-ct]
            break    
    ext.append(temp[::-1])
    ct = 1



#Prompts user to select destination folder to copy the renamed files to. Stores the path to the dest variable.
print("Select where you want to save the renamed file")
time.sleep(2)
dest = askdirectory() + "/"
new_name = input("Enter the new name for the file\n")


# For Loop that formats the new name of the file(s) and adds them to a list (f_dest) 
number = 1
f_dest = []
for b in ext:
    string = dest + new_name + "_" + str(number) + str(b)
    f_dest.append(string)
    number += 1



for y in range(len(target)):
    shutil.copyfile(target[y], f_dest[y])
    number += 1

