# Joseph Melancon
# joseph@jmelancon.com
# 2022

'''get all music files in a directory and convert them via ffmpeg'''

import os
import sys

import filetypes
import menuutils


def find_files(music_dir, extensions):
    '''scan a provided directory for files. if a folder is found, recurse.'''
    dir_array = os.listdir(
        music_dir)  # uses listdir to get any files in that directory as an array
    file_array = []  # make an empty array for us to put full file paths in

    for each in dir_array:  # where the magic happens

        new_path = music_dir  # start with our base directory for the new file path
        if new_path[-1] != "/":  # if there isn't a / at the end of the path, we must add one
            new_path += "/"  # boom
        new_path += each  # add our file or folder to new_path to get its full path

        if os.path.isdir(new_path):  # if we have a folder, we must recurse.
            # print a simple status message
            # print(new_path + " is a directory! Scanning it too...") #old debug
            file_array += find_files(new_path, extensions)  # recurse!

        else:  # if it's not a directory, then it must be a file!
            # lol this is awful. split the path at the periods
            get_extension_split = each.split(".")
            # check if we should put it on the list
            if get_extension_split[-1] in extensions:
                file_array.append(new_path)  # add it to our list of files.

    # return the array. if recursing, this is added to the parent's file_array.
    return file_array


def specify_ffmpeg():
    '''ask the user where their ffmpeg install is'''
    while 1 == 1:
        try:
            ffmpeg_dir = str(
                input("please type either your ffmpeg dir or 'quit'\n>>> "))
            if os.path.exists(ffmpeg_dir):
                print("ok! using specified ffmpeg binary.")
                return ffmpeg_dir
            elif ffmpeg_dir.lower() == "quit":
                print("goodbye!")
                exit()
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            print(
                "that is not an existing file. please specify the full path to an ffmpeg binary.")


def find_ffmpeg():
    '''reports if the system has ffmpeg installed'''
    #add windows support soon(tm)
    #no mac support because i don't have that
    if sys.platform == "linux" and os.path.exists("/bin/ffmpeg"):
        print("found ffmpeg install at /bin/ffmpeg")
        return "/bin/ffmpeg"
    elif sys.platform == "linux":
        print("!! i did not find ffmpeg on your system.")
        return specify_ffmpeg()


def run_ffmpeg(ffmpeg_dir, input_file, args, output_file):
    '''run ffmpeg'''

def prompt_for_args():
    '''prompt the user to input arguments'''
    args = str("")
    print("please enter the output file's bitrate in kbps. enter '0' for no bitrate change.")
    while 1==1:
        try:
            bitrate = int(input("new bitrate:\n>>> "))
            break
        except ValueError:
            print("sorry, that doesn't look like a whole number. try again please!")
    if bitrate != 0:
        args += str("-ab " + bitrate + "k ")
    strip_art = str(input("strip music album art? (y/N)\n>>> "))
    if strip_art.lower() == "y":
        args += str("—vn ")
    return args

def prompt_file_inputs():
    '''propmps for file searching'''
    music_dir = str(input("\ninput music dir.\n>>> "))
    print("\navailable formats:\n")
    for line in filetypes.format_dict_music.keys():
        print(line)
    print()
    # filetypes.format_dict_music["ogg-vorbis"]
    formats_to_use = str(
        input("gimmie formats, multiple separated by commas, no space.\n>>> "))
    file_exts = []
    for each in formats_to_use.split(","):
        file_exts += filetypes.format_dict_music[each]
    file_array = find_files(music_dir, file_exts)
    do_printfiles = str(input("should i print the files i found? (y/N)\n>>> "))
    if do_printfiles.lower() == "y":
        for each in file_array:
            print(each)
    return file_array

def prompt_file_output():
    '''ask the user how they want the output files'''
    available_formats = []
    for line in filetypes.format_dict_music.values():
        available_formats += line
    print("available output options:\n")
    for each in available_formats:
        print(each)
    print("\nplease select one format for all output files.")
    while 1==1:
        try:
            sel = str(input("file type:\n>>> "))
            if sel in available_formats:
                file_format = sel
                break
            else: raise ValueError
        except ValueError:
            print("\nsorry, i need a format on the list. please try again.\n")
    print("\nok. now, what output structure would you like?")
    print("1 - parallel: make a new folder. same directory structure.")
    print("2 - in-place: each file goes into the same directory as the original.")
    sel = menuutils.integerSelection(1,2)
    return [file_format, sel]

def transform_outputs(input_array, output_type, orig_path, format_ext):
    '''take our input array and transform it for output structure'''
    output_array = []
    if output_type == int(1): #parallel
        print("parallel")
    elif output_type == int(2): #in-place
        print("in-place")
        

def main():
    '''run other functions'''
    #ffmpeg_dir = find_ffmpeg()
    #file_array = prompt_file_inputs()
    #args = prompt_for_args()
    #file_output
    #output_options = prompt_file_output()


if __name__ == "__main__":
    main()
