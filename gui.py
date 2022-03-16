# jmelancon
# joseph@jmelancon.com
# 2022

import fileops
import filetypes

from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


def show_foundfiles():
    file_array = fileops.find_files(music_dir_orig, formats_array)
    out = ""
    for each in file_array:
        out += each + "\n"
    showinfo(
        title='Music found:',
        message=out
    )


def select_file():
    global music_dir_orig
    music_dir_orig = fd.askdirectory(
        title='Select Music Directory...',
        initialdir='/')
    selectionmessage = "You have selected the directory "
    showinfo(
        title='Directory Selected!',
        message=selectionmessage + music_dir_orig
    )


def format_checkbox_upd():
    formats = []
    global formats_array
    if checkbox_flac.get() != "":
        formats += filetypes.format_dict_music[checkbox_flac.get()]
    if checkbox_mp3.get() != "":
        formats += filetypes.format_dict_music[checkbox_mp3.get()]
    if checkbox_ogg.get() != "":
        formats += filetypes.format_dict_music[checkbox_ogg.get()]
    if checkbox_msft.get() != "":
        formats += filetypes.format_dict_music[checkbox_msft.get()]
    if checkbox_apple.get() != "":
        formats += filetypes.format_dict_music[checkbox_apple.get()]
    formats_array = formats
    print(formats)


def select_directory_window():
    global music_dir_orig
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="File Selection").grid(column=0, row=0)
    ttk.Button(frm, text="Open Input Directory",
               command=select_file).grid(column=0, row=1)
    ttk.Label(frm, text=music_dir_orig).grid(column=0, row=1)
    ttk.Button(frm, text="Continue",
               command=root.destroy).grid(column=0, row=2)
    print(music_dir_orig)
    root.mainloop()
    print(music_dir_orig)


music_dir_orig = ""
select_directory_window()
