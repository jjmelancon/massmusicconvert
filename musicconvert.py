#!/usr/bin/env python3

# jmelancon
# joseph@jmelancon.com
# 2022

'''get all music files in a directory and convert them via ffmpeg'''

import os
import sys
import subprocess

import syscheck
import fileops
import guidedcli
import gui
import multiexec
from colors import colortext


def execute_ffmpeg(ffmpeg_dir, io_dict, args, ffprobe_dir):
    '''run ffmpeg. this is deprecated, use multiexec's execute funciton.'''
    # special case for windows because it is annoying
    # they really like their backlashes and quotes around spaces
    # so the path has to be doctored before we run ffmpeg_dir
    if syscheck.platform == "win32":
        ffmpeg_dir = fileops.prep_dir_win(ffmpeg_dir, False)
        if ffprobe_dir != "":
            ffprobe_dir = fileops.prep_dir_win(ffprobe_dir, False)
    # so for each key in the input/output dictionary, which will be an input,
    # we will use the key (input) to get the value (output), then splice that
    # all into a command string to run via ffmpeg on *nix systems
    for input_dir in io_dict.keys():
        tmp_args = args
        # check if directories exist first!!!
        # see fileops.missing_dir_test_nix()
        output_dir = io_dict[input_dir]
        fileops.missing_dir_test(output_dir)
        # if user wanted to retain source bitrate, we need to get it now.
        # we'll use ffprobe to get the bitrate, then append it to the args
        # variable.
        if ffprobe_dir != "":
            ffprobe_args = "-show_entries format=bit_rate -hide_banner -loglevel quiet"
            print(ffprobe_dir)
            print('"{}" {} "{}"'.format(ffprobe_dir, ffprobe_args, io_dict[input_dir]))
            bitrate = subprocess.getoutput('"{}" {} "{}"'.format(ffprobe_dir, ffprobe_args, input_dir))[18:-10]
            print(bitrate)
            bitrate_usable = int(bitrate) // 1000
            tmp_args += str("-ab " + str(bitrate_usable) + "k ")
        # {ffmpeg} -i "{input}" {arguments}"{output}"
        # note that the arguments string has a space at the end by default
        if syscheck.platform == "linux" or syscheck.platform == "unix":
            command = str('"{}" -i "{}" {}"{}"'.format(
                ffmpeg_dir, input_dir, tmp_args, io_dict[input_dir]))
        else:
            command = str('{} -i "{}" {}"{}"'.format(
                ffmpeg_dir, fileops.prep_dir_win(input_dir, False), tmp_args,
                fileops.prep_dir_win(io_dict[input_dir], False)))
        # moment of truth
        #print("\n\nDEBUG\nNEW PATH:\n" + io_dict[input_dir] + "\nBITRATE:\n" + str(bitrate_usable) + "\nCOMMAND:")
        #print(command)
        os.system(command)


def parse_args(args_array):
    '''parse arguments that are passed through via the command line'''
    possible_modes = [
        "--gcli",
        "--cli",
        "--gui"
    ]
    if len(args_array) == 1:
        # assume guided cli
        print(colortext("\nno arguments passed, assuming guided cli...\n","purple",style="i"))
        return "--gcli"
    elif len(args_array) > 2 and args_array[1] == "--cli":
        # implement soon (tm)
        print("not finished. use --gcli.")
        exit()
    elif len(args_array) == 2 and args_array[1] in possible_modes:
        # return the mode
        return args_array[1]
    elif len(args_array) == 2 and args_array[1] == "--help":
        # give help
        print("massmusicconvert. args: --gcli, --cli, --gui")
        exit()
    else:
        # bad args
        print("bad args. run with --help for help.")
        print(args_array)
        exit()


def main():
    '''run other functions'''
    output_mode = parse_args(sys.argv)

    if output_mode == "--gcli":
        docs_url = "https://massmusicconvert.jmelancon.com/usage/"
        print(colortext("before jumping in, be sure to read the docs at {}\n".format(docs_url),"purple",style="i"))
        ffmpeg_dir = syscheck.find_ffmpeg()

        file_array_pkg = guidedcli.prompt_file_inputs()  # needs to be unpacked
        # array of files that needs to be converted
        file_array = file_array_pkg[0]
        orig_path = file_array_pkg[1]  # path that we asked the user for

        args_array = guidedcli.prompt_for_args()  # output args, ffprobe path

        output_options_pkg = guidedcli.prompt_file_output()  # get output opts
        format_ext = output_options_pkg[0]  # file extensions
        dir_struct_type = output_options_pkg[1]  # parallel or in-place

        output_info = guidedcli.transform_outputs(
            file_array, dir_struct_type, orig_path, format_ext)
        
        output_dict = output_info[0]
        new_path = output_info[1]
        
        guidedcli.confirm_choices(orig_path, new_path, format_ext)

        multiexec.execute_ffmpeg_split(ffmpeg_dir, output_dict, args_array[0], args_array[1])

        print(colortext("\n!!! MUSIC CONVERSION COMPLETE !!!\n", "purple", style="b"))
    elif output_mode == "--gui":
        gui.main()
    elif output_mode == "--cli":
        print(colortext("not yet implemented, sorry :(", "red"))
        exit()


if __name__ == "__main__":
    main()
