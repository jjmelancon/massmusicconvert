# jmelancon
# joseph@jmelancon.com
# 2022

import menuutils
import syscheck
import filetypes
import fileops


def prompt_file_inputs():
    '''propmps for file searching'''
    if syscheck.platform == 'win32':
        print("input your music directory below starting with 'c:/'.")
        print("use '/' instead of '\\' please!")
    else:
        print("please input your music directory below.")
    music_dir = str(input("\nmusic dir:\n>>> "))
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
    file_array = fileops.find_files(music_dir, file_exts)
    do_printfiles = str(input("should i print the files i found? (y/N)\n>>> "))
    if do_printfiles.lower() == "y":
        for each in file_array:
            print(each)
    return [file_array, music_dir]


def prompt_for_args():
    '''prompt the user to input arguments'''
    # start by making a string for our arguments
    args = str("")
    # '-vn' means '-(video)(no)'.
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
