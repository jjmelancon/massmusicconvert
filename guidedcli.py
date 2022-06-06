# jmelancon
# joseph@jmelancon.com
# 2022

import menuutils
import syscheck
import filetypes
import fileops
from colors import colortext


def prompt_file_inputs():
    '''prompts for file searching'''
    while True:
        if syscheck.platform == 'win32':
            print(colortext("input your music directory below starting with the proper drive letter.", "cyan"))
            print(colortext("remember, follow the directory structure outlined in the docs!", "cyan"))
        else:
            print(colortext("please input your music directory below.", "cyan"))
            print(colortext("remember, follow the directory structure outlined in the docs!", "cyan"))
        music_dir = str(input(colortext("\nmusic dir:\n>>> ","yellow")))

        if fileops.dir_exists_test(music_dir):
            print(colortext("\ndirectory exists. continuing.\n", "green"))
            break
        else:
            print(colortext("\nthis directory does not exist. please check input.\n", "red"))
    print(colortext("available formats:", "cyan"))
    for line in filetypes.format_dict_music.keys():
        print(colortext("  • {}".format(line), "blue"))
    print()
    while 1==1:
        print(colortext("list the formats you want separated by commas with no space.", "cyan"))
        print(colortext("alternatively, you can type \"all\" to select all music types.\n", "cyan"))
        formats_to_use = str(
            input(colortext("formats desired:\n>>> ", "yellow")))
        file_exts = []
        available_formats = []  # make an array for listing possible file types
        # run those bad boys in the format dict off
        for line in filetypes.format_dict_music.keys():
            available_formats.append(line)
        if formats_to_use == "all":
            for each in filetypes.format_dict_music.keys():
                file_exts += filetypes.format_dict_music[each]
            break
        else:
            formats_bad = False
            file_exts = []
            for each in formats_to_use.split(","):
                if each in available_formats:
                    file_exts += filetypes.format_dict_music[each]
                else:
                    print(colortext("\nsorry, looks like you made a typo!", "red"))
                    print(colortext("\"{}\" is not a valid file format.\n".format(each), "red"))
                    formats_bad = True
            if not formats_bad:
                break


    file_array = fileops.find_files(music_dir, file_exts)
    print(colortext("\ndo you want to read a list of discovered files?", "cyan"))
    print(colortext("just a heads up, this list is usually REALLY long.\n", "cyan"))
    do_printfiles = str(input(colortext("list files? (y/N)\n>>> ", "yellow")))
    if do_printfiles.lower() == "y":
        print(colortext("\ndiscovered files:\n", "blue"))
        for each in file_array:
            print(each)
        print(colortext("\ntotal files found: {}".format(len(file_array)), "blue"))
    return [file_array, music_dir]


def prompt_for_args():
    '''prompt the user to input arguments'''
    # start by making a string for our arguments
    args = str("")
    # '-vn' means '-(video)(no)'.
    # this will remove the art from the file!
    print(colortext("\ndo you want to remove any cover images from processed songs?", "cyan"))
    print(colortext("oftentimes people keep their art, but it may save some space to remove it.\n", "cyan"))
    strip_art = str(input(colortext("strip art? (y/N)\n>>> ", "yellow")))
    # if it's not 'y' or 'Y', we do not care.
    if strip_art.lower() == "y":
        # trailing space to make adding the next argument less of a pain.
        # we correct for the additional space when we execute.
        args += str("-vn ")
    # now for bitrate
    print(colortext("\nwould you like to change the output file's bitrate?", "cyan"))
    print(colortext("reducing bitrate can save lots of space but will reduce audio quality.", "cyan"))
    print(colortext("enter a new bitrate here (ex. \"320\") or enter \"0\" to leave bitrates unchanged.\n", "cyan"))
    # use try/except to get an int
    while 1 == 1:
        try:
            bitrate = int(input(colortext("new bitrate:\n>>> ", "yellow")))
            # not testing for a high value because i'm lazy
            break
        except ValueError:
            #  make them try again
            print(colortext("\nsorry, that doesn't look like a whole number.\n", "red"))
    if bitrate == 0:
        # todo: check if ffprobe is in the same dir as ffmpeg before asking for it
        ffprobe_location = syscheck.find_ffprobe()
    else:
        args += str("-ab " + str(bitrate) + "k ")
        ffprobe_location = ""
    return [args, ffprobe_location]


def transform_outputs(input_array, output_type, orig_path, format_ext):
    '''take our input array and transform it for output structure'''
    output_array = []
    # we need to sanitize the path so we can figure out its length
    orig_path = fileops.dir_sanitizer(orig_path)
    # add a "/" if it is not at the end of the path
    if orig_path[-1] != "/":
        orig_path += "/"
    if output_type == int(1):  # parallel
        # if we can get the length of the original path, we can cut it off
        # by cutting off the first x characters of the input file, which will
        # always be the length of orig_path

        orig_path_len = int(len(orig_path))

        # get the new directory and add a '/' if nessesary at the end
        print(colortext("\nfor parallel directories, we'll need a new place for output files.", "cyan"))
        print(colortext("directories are created automatically if they don't exist,", "cyan"))
        print(colortext("so be careful that you aren't making any typos.\n", "cyan"))
        new_dir = str(input(colortext("new music dir:\n>>> ", "yellow")))
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
        new_dir = orig_path
        # same as parallel but we only change the extension! easy peasy.
        output_array = []  # make an array for our output dirs

        for old_path in input_array:  # input path processing
            # cut old extension off of new_stub
            # see the parallel option to see why this is awful
            old_path_split = old_path.split(".")  # split it up
            chars_to_chop = len(old_path_split[-1]) + 1  # add 1 for '.'
            # save our work on top of new_stub
            new_out_path = old_path[:-chars_to_chop] + "_converted." + format_ext
            # save to output_array
            output_array.append(new_out_path)
    # i don't know how this works but it does lol
    ffmpeg_files_dict = dict(zip(input_array, output_array))
    return [ffmpeg_files_dict, new_dir]


def prompt_file_output():
    '''ask the user how they want the output files'''
    # this is mostly just on a rail asking the user for input
    available_formats = []  # make an array for listing possible file types
    # run those bad boys in the format dict off
    for line in filetypes.format_dict_music.values():
        available_formats += line
    # do basically the same thing again
    print(colortext("\navailable output options:", "cyan"))
    for each in available_formats:
        print(colortext("  • {}".format(each), "blue"))
    print(colortext("\nplease select one format type for all output files.\n", "cyan"))
    # we need to get something that is already on the list, so try/except ftw
    while 1 == 1:
        try:
            sel = str(input(colortext("file type:\n>>> ", "yellow")))
            if sel in available_formats:
                file_format = sel
                break
            else:
                raise ValueError
        except ValueError:
            print(colortext("\nsorry, i need one of the formats on the list. please try again.\n", "red"))
    # as i said, mostly on a rail
    print(colortext("\nok. now, what output structure would you like?", "cyan"))
    print(colortext("  1: parallel: make a new folder. same directory structure.", "blue"))
    print(colortext("  2: in-place: each file goes into the same place as the original\n", "blue"))
    # see menuutils for how this works
    sel = menuutils.integer_selection(1, 2)
    # bundle it up and ship it off!
    return [file_format, sel]

def confirm_choices(input_dir, output_dir, file_format):
    print(colortext("the program is now ready to convert your music.", "cyan"))
    print(colortext("before we continue though, please confirm that the following is correct:", "cyan"))
    print(colortext("  • input folder: {}".format(fileops.dir_sanitizer(input_dir)), "blue"))
    print(colortext("  • output folder: {}".format(output_dir), "blue"))
    print(colortext("  • output type: {}".format(file_format), "blue"))
    print(colortext("\nif you are ready to continue, please type", "cyan"),
        colortext("\"YES\"", "red", style="b"),
        colortext("to confirm your choices.", "cyan"))
    while 1==1:
        ready = input(colortext("\nare you ready?\n>>> ", "yellow"))
        if ready == "YES":
            print(colortext("\n!!! STARTING MUSIC CONVERSION !!!\n", "purple", style="b"))
            break