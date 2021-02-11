import os
import shutil
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilenames, askdirectory
import time


Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
#filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
#print(filename)


print("Select the files you want to rename")

time.sleep(2)

target = list(askopenfilenames())

ext = []

for a in target:
    ext.append(a[-4:])

print("Select where you want to save the renamed file")

time.sleep(2)

dest = askdirectory() + "/"

new_name = input("Enter the new name for the file\n")

number = 1

'''
print("Proceed with renaming this file?\nHit enter")

for x in target:

    print("{}   ------->  {}_{}{}".format(x, new_name, number, ext))
    number += 1

input()
'''
f_dest = []

'''
print(type(new_name))

print(type("_"))

print(type(str(number)))

print(type(ext))

input()
'''
for x in target:
    for b in ext:
        string = dest + new_name + "_" + str(number) + str(b)
    f_dest.append(string)
    number += 1

number = 1



for y in range(len(target)):
    shutil.copyfile(target[y], f_dest[y])
    number += 1

