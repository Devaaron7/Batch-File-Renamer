import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askopenfilenames, askdirectory
import time

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
#filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
#print(filename)

print("Select the files you want to rename")

time.sleep(2)

target = list(askopenfilenames())

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
        #ext.append(a[-4:])

print("Select where you want to save the renamed file")

time.sleep(2)

dest = askdirectory() + "/"

new_name = input("Enter the new name for the file\n")

number = 1

f_dest = []

for x in target:
    for b in ext:
        string = dest + new_name + "_" + str(number) + str(b)
    f_dest.append(string)
    number += 1

number = 1

for y in range(len(target)):
    shutil.copyfile(target[y], f_dest[y])
    number += 1

