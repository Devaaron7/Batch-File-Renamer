import os
import shutil
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename, askdirectory
import time


Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
#filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
#print(filename)


print("Select the file you want to rename")

time.sleep(2)

target = askopenfilename()

ext = target[-4:]

print("Select where you want to save the renamed file")

time.sleep(2)

dest = askdirectory() + "/"

new_name = input("Enter the new name for the file\n")


print("Proceed with renaming this file?\nHit enter")

input("{}   ------->  {}".format(target, new_name + ext))


#os.rename(target, "B/{}".format(new_name + ext))

print(dest + new_name + ext)

shutil.copyfile(target, dest + new_name + ext)
