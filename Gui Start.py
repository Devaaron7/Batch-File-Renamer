from tkinter.constants import HORIZONTAL, N, WORD
from guizero import App, ListBox, MenuBar, TextBox, Text, Combo, PushButton, Box
import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askopenfilenames, askdirectory
from tkinter.ttk import Progressbar
import time
import winsound


def file_name(file_path):
    clean_file_names = []
    clean_file_name = ""
    for items in file_path:
        for words in items[::-1]:
            if words != "/":
                clean_file_name += words
            else:
                break         
        clean_file_names.append(clean_file_name[::-1])
        clean_file_name = ""
    return clean_file_names


def load_file_and_save_dir():
    if len(selected_file_list) != 0:
        selected_file_list.clear()
    temp_file_list = (list(askopenfilenames(title="Select Files To Rename")))
    for items in temp_file_list:
        selected_file_list.append(items)
    save_dir = (askdirectory(title="Select Where To Save The Renamed Files") + "/")
    #save_alert_text.enable()
    app.title = "File Renamer  -  Saving To - " + str(save_dir)
    list_box_left.clear()
    dir_text.value = str(save_dir)
    index_for_box_left = 0
    for index_for_selected_file_list in range(len(selected_file_list)):
        list_box_left.insert(index_for_box_left, file_name(selected_file_list)[index_for_selected_file_list])
        index_for_box_left += 1

def constant_updated_type_box_right():
    list_box_right.clear()
    index_for_box_right = 0
    counter_for_alp_list = 0
    for i in range(len(list_box_left.items)):
        list_box_right.insert(index_for_box_right, input_box_a.value + "_" + alp_list[counter_for_alp_list])
        index_for_box_right += 1
        counter_for_alp_list += 1
        
        
def combo_box_b_selection(selected_value):
    index_for_box_right = 0
    counter_for_num_list = 0
    counter_for_alp_list = 0
    list_box_right.clear()
    if selected_value == "1,2,3..":
        for i in range(len(list_box_left.items)):
            list_box_right.insert(index_for_box_right, input_box_a.value + "_" + str(num_list[counter_for_num_list]))
            index_for_box_right += 1
            counter_for_num_list += 1
    if selected_value == "A,B,C..":
        for i in range(len(list_box_left.items)):
            list_box_right.insert(index_for_box_right, input_box_a.value + "_" + alp_list[counter_for_alp_list])
            index_for_box_right += 1
            counter_for_alp_list += 1
    if selected_value == "1 of X..":
        for i in range(len(list_box_left.items)):
            list_box_right.insert(index_for_box_right, input_box_a.value + "_" + str(num_list[counter_for_num_list]) + "_of_" + str(len(list_box_left.items)))
            index_for_box_right += 1
            counter_for_num_list += 1


def pbar(num_of_items):
    units = 100 / num_of_items
    if pb['value'] < 100:
        pb['value'] += units
        pb.update_idletasks()
        time.sleep(.1)
    elif pb['value'] >= 100:
        pb.stop()


def run_program():
    num_of_files = len(selected_file_list)
    #num_of_files = 5
    for index_left_and_right_box in range(len(selected_file_list)):
        shutil.copyfile(selected_file_list[index_left_and_right_box], dir_text.value + list_box_right.items[index_left_and_right_box] + list_box_left.items[index_left_and_right_box][-4:])
        pbar(num_of_files)
    winsound.PlaySound("notify.wav", winsound.SND_FILENAME)



num_list = list(range(1, 27))
alp_list = list("abcdefghijklmnopqrstuvwxyz".upper())
selected_file_list = []


app = App(width = 750, title="File Renamer")

list_box_left = ListBox(app, width = 250, items=["a list"], height="fill", align="left")
list_box_right = ListBox(app, width = 250, items=["b list"], height="fill", align="right")


static_text_box_a = Text(app, text="Enter Name For New Files")
input_box_a = TextBox(app, command=None)
input_box_a.update_command(constant_updated_type_box_right)


static_text_box_b = Text(app, text="Choose A Suffix")
combo_box_b = Combo(app, options=["1,2,3..", "A,B,C..", "1 of X.."], command=combo_box_b_selection)


#save_alert_text = Text(app, width = "fill", text="Saving to...")
#save_alert_text.disable()

dir_text = Text(app, width = "fill", text="")

run_button = PushButton(app, text="Start Program!", command=run_program)


menubar = MenuBar(app,
                  toplevel=["File"],
                  options=[
                      [ ["Select Files..", load_file_and_save_dir],]
                  ])


box = Box(app, border=False)

# add a progress bar to the box
pb = Progressbar(box.tk, length=1000)
box.add_tk_widget(pb)

app.display()

