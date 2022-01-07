# jmelancon
# joseph@jmelancon.com
# 2022

'''get all music files in a directory and convert them via ffmpeg'''

import os
import sys
from pathlib import Path

import filetypes
import menuutils


def find_files(music_dir, extensions):
    '''scan a provided directory for files. if a folder is found, recurse.'''
    dir_array = os.listdir(
        music_dir)  # uses listdir to get any files in that dir as an array
    file_array = []  # make an empty array for us to put full file paths in

    for each in dir_array:  # where the magic happens

        new_path = music_dir  # start with our base directory for the new path
        if new_path[-1] != "/":  # if there's no / at the end, fix it
            new_path += "/"  # boom
        new_path += each  # add our file or folder to new_path to get its path

        if os.path.isdir(new_path):  # if we have a folder, we must recurse.
            # print a simple status message
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
    # start a loop because the user may input a bad/nonexistent file location
    while 1 == 1:
        # try/except for if a bad file path is supplied
        try:
            # ask for the path
            f_d = str(input("please type ffmpeg's directory or 'quit'\n>>> "))
            # if a user realizes they don't have ffmpeg, they can just leave
            # we'll test this first because a user may have a file called quit
            elif ffmpeg_dir.lower() == "quit":
                print("goodbye!")
                exit()
            # os.path.exists is able to check if this is a real location
            # todo: make it work on windows
            if os.path.exists(ffmpeg_dir):
                print("ok! using specified ffmpeg binary.")
                return ffmpeg_dir
            # if neither of these are correct, we didn't find a file.
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            print("that is not an existing file.")
            print("please specify the full path to an ffmpeg binary.")


def find_ffmpeg():
    '''reports if the system has ffmpeg installed'''
    # add windows support soon(tm)
    # mac support is very tenative at the moment, idk
    # linux support is my main focus as an Arch user btw

    # this case is the easiest. ffmpeg at default location on linux.
    if sys.platform == "linux" and os.path.exists("/bin/ffmpeg"):
        print("found ffmpeg install at /bin/ffmpeg")
        return "/bin/ffmpeg"

    # this is harder. windows uses non standard path separators,
    # so windows will be a pain in my figurative rear end to
    # implement. stay tuned.
    # just exit so i don't have to fix it now.
    elif sys.platform == "win32":
        print("windows is not supported at this time.\ngoodbye!")
        exit()

    # darwin is the codename for apple's macos kernel.
    # thanks to macos being unix, the linux commands in this script
    # should just work(tm) on macos.
    # todo: add ffmpeg default install location for mac
    elif sys.platform == "darwin":
        print("!! i have not yet tested macos!")
        print("please manually specify where your ffmpeg binary is.")
        return specify_ffmpeg()

    # everyone's linux distro has some odd, nonstandard bs,
    # so if the platform is linux and ffmpeg isn't in /bin/,
    # we'll ask the user.
    elif sys.platform == "linux":
        print("!! i did not find ffmpeg on your system.")
        return specify_ffmpeg()

    # i only plan on doing operating systems on a whitelist basis,
    # so if the above fail, just exit.
    else:
        print("sorry, your platform is not supported by this script.")
        exit()


def missing_dir_test_nix(file_path):
    '''test if a dir exists from a file path. if it does not, make it!'''
    # start by splitting the path by slashes. this is not win32 compatable!
    split_file_dir = file_path.split("/")
    # chop off the last block of the array. this will be the file.
    split_file_dir.pop()
    # now, rejoin the array with slashes
    test_dir = "/".join(split_file_dir)
    # now we can create a Path object
    p = Path(test_dir)
    # if our path object doesn't exist, there is no real directory for what we
    # want. thus, we must make it!
    if not p.exists():
        # first, we tell the user it does not exist. this will be lost
        # in a sea of ffmpeg output, but i do not care.
        print("'{}' does not exist! creating now...".format(test_dir))
        # on *nix systems, mkdir -p will recursively create directories.
        # this is good if, for example, the user uses window media player.
        # windows media player will put the music in an album folder that
        # is itself in an artist folder. this ensures that both the artist
        # and album folders are made.
        os.system('mkdir -p "{}"'.format(test_dir))


def execute_ffmpeg(ffmpeg_dir, io_dict, args):
    '''run ffmpeg'''
    # so for each key in the input/output dictionary, which will be an input,
    # we will use the key (input) to get the value (output), then splice that
    # all into a command string to run via ffmpeg on *nix systems
    for input_dir in io_dict.keys():
        # check if directories exist first!!!
        # see missing_dir_test_nix()
        output_dir = io_dict[input_dir]
        missing_dir_test_nix(output_dir)
        # {ffmpeg} -i "{input}" {arguments}"{output}"
        # note that the arguments string has a space at the end by default
        command = str('{} -i "{}" {}"{}"'.format(
            ffmpeg_dir, input_dir, args, io_dict[input_dir]))
        # moment of truth
        os.system(command)


def prompt_for_args():
    '''prompt the user to input arguments'''
    # start by making a string for our arguments
    args = str("")
    # what '-vn' does means '-(video)(no)'.
    # this will remove the art from the file!
    strip_art = str(input("strip music album art? (y/N)\n>>> "))
    # if it's not 'y' or 'Y', we do not care.
    if strip_art.lower() == "y":
        # trailing space to make adding the next argument less of a pain.
        # we correct for the additional space when we execute.
        args += str("-vn ")
    # now for bitrate
    print("please enter the output file's bitrate in kbps.")
    print("enter '0' to let ffmpeg choose.")
    # todo: create 1:1 bitrate option
    # use try/except to get an int
    while 1 == 1:
        try:
            bitrate = int(input("new bitrate:\n>>> "))
            # not testing for a high value because i'm lazy
            break
        except ValueError:
            #  make them try again
            print("sorry, that doesn't look like a whole number.")
    if bitrate != 0:
        args += str("-ab " + str(bitrate) + "k ")
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
    return [file_array, music_dir]


def prompt_file_output():
    '''ask the user how they want the output files'''
    # this is mostly just on a rail asking the user for input
    available_formats = []  # make an array for listing possible file types
    # run those bad boys in the format dict off
    for line in filetypes.format_dict_music.values():
        available_formats += line
    # do basically the same thing again
    print("available output options:\n")
    for each in available_formats:
        print(each)
    print("\nplease select one format for all output files.")
    # we need to get something that is already on the list, so try/except ftw
    while 1 == 1:
        try:
            sel = str(input("file type:\n>>> "))
            if sel in available_formats:
                file_format = sel
                break
            else:
                raise ValueError
        except ValueError:
            print("\nsorry, i need a format on the list. please try again.\n")
    # as i said, mostly on a rail
    print("\nok. now, what output structure would you like?")
    print("1 - parallel: make a new folder. same directory structure.")
    print("2 - in-place: each file goes into the same place as the original.")
    # see menuutils for how this works
    sel = menuutils.integer_selection(1, 2)
    # bundle it up and ship it off!
    return [file_format, sel]


def transform_outputs(input_array, output_type, orig_path, format_ext):
    '''take our input array and transform it for output structure'''
    output_array = []
    # add a "/" if it is not at the end of the path
    if orig_path[-1] != "/":
        orig_path += "/"
    if output_type == int(1):  # parallel
        # if we can get the length of the original path, we can cut it off
        # by cutting off the first x characters of the input file, which will
        # always be the length of orig_path

        orig_path_len = int(len(orig_path))

        # get the new directory and add a '/' if nessesary at the end

        new_dir = str(input("\ninput new music dir.\n>>> "))
        if new_dir[-1] != "/":
            new_dir += "/"

        output_array = []  # make an array for our output dirs

        for old_path in input_array:  # input path processing
            # start by cutting off old path
            new_stub = old_path[orig_path_len:]
            # cut old extension off of new_stub
            # this code is awful because we can't just split at periods
            # example: "J. Cole" has a period in the artist name.
            # instead, we can split at periods, take the length of
            # the last item, then chop it off of the end of new_stub
            new_stub_split = new_stub.split(".")  # split it up
            chars_to_chop = len(new_stub_split[-1]) + 1  # add 1 for '.'
            # save our work on top of new_stub
            new_stub = new_stub[:-chars_to_chop] + "." + format_ext
            # finally, get our output path
            new_out_path = new_dir + new_stub
            # save to output_array
            output_array.append(new_out_path)
    elif output_type == int(2):  # in-place
        # same as parallel but we only change the extension! easy peasy.
        output_array = []  # make an array for our output dirs

        for old_path in input_array:  # input path processing
            # cut old extension off of new_stub
            # see the parallel option to see why this is awful
            old_path_split = old_path.split(".")  # split it up
            chars_to_chop = len(old_path_split[-1]) + 1  # add 1 for '.'
            # save our work on top of new_stub
            new_out_path = old_path[:-chars_to_chop] + "." + format_ext
            # save to output_array
            output_array.append(new_out_path)
    # i don't know how this works but it does lol
    ffmpeg_files_dict = dict(zip(input_array, output_array))
    return ffmpeg_files_dict


def main():
    '''run other functions'''
    ffmpeg_dir = find_ffmpeg()

    file_array_pkg = prompt_file_inputs()  # needs to be unpacked below
    file_array = file_array_pkg[0]  # array of files that needs to be converted
    orig_path = file_array_pkg[1]  # path that we asked the user for

    args = prompt_for_args()  # to be used for output. bitrate, retain art, etc

    output_options_pkg = prompt_file_output()  # get our output options. array
    format_ext = output_options_pkg[0]  # file extensions
    dir_struct_type = output_options_pkg[1]  # parallel or in-place

    output_dict = transform_outputs(
        file_array, dir_struct_type, orig_path, format_ext)

    execute_ffmpeg(ffmpeg_dir, output_dict, args)


if __name__ == "__main__":
    main()
