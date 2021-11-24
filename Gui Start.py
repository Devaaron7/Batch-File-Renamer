from tkinter.constants import N, WORD
from guizero import App, ListBox, MenuBar, TextBox, Text, Combo, PushButton
import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askopenfilenames, askdirectory


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
    temp_file_list = (list(askopenfilenames(title="Select Files To Rename")))
    for items in temp_file_list:
        selected_file_list.append(items)
    save_dir = (askdirectory(title="Select Where To Save The Renamed Files") + "/")
    save_dir_alert.value= "Saving to...\n" + str(save_dir)
    list_box_left.clear()
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


def run_program():
    print(selected_file_list)
    
    print(save_dir_alert.value) + str(file_name(selected_file_list))
    #for y in range(len(selected_file_list)):
    #    shutil.copyfile(selected_file_list[y], save_dir + file_name(selected_file_list)[y])
    #    #print(save_dir + file_name(selected_file_list)[y])


num_list = list(range(1, 27))
alp_list = list("abcdefghijklmnopqrstuvwxyz".upper())
selected_file_list = []
#save_dir = ""

app = App(width = 750)

list_box_left = ListBox(app, width = 250, items=["a list"], height="fill", align="left")
list_box_right = ListBox(app, width = 250, items=["b list"], height="fill", align="right")


static_text_box_a = Text(app, text="Enter Name For New Files")
input_box_a = TextBox(app, command=None)
input_box_a.update_command(constant_updated_type_box_right)


static_text_box_b = Text(app, text="Choose A Suffix")
combo_box_b = Combo(app, options=["1,2,3..", "A,B,C..", "1 of X.."], command=combo_box_b_selection)

#save_button = PushButton(app, text="Select Save Folder", command=save_dir)
save_dir_alert = Text(app, width = "fill", text="")


#run_button = PushButton(app, text="Start Program!", command=run_program)

run_button = PushButton(app, text="Start Program!", command=run_program)


menubar = MenuBar(app,
                  toplevel=["File"],
                  options=[
                      [ ["Select Files..", load_file_and_save_dir],]
                  ])



app.display()

