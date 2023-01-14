#!/usr/bin/env python3

# jmelancon
# joseph@jmelancon.com
# 2023

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

        reusing = False
        if os.path.exists("conversiondata.db"):
            imported_data = guidedcli.sqlite_import()
            if imported_data is not None:
                reusing = True
                orig_path, new_path, input_filetypes, output_filetype, output_dict, args_array, preset, prunelist = imported_data
        if not reusing:
            file_array, orig_path, input_filetypes = guidedcli.prompt_file_inputs()  # needs to be unpacked

            args_array = guidedcli.prompt_for_args()  # output args, ffprobe path

            output_filetype, dir_struct_type = guidedcli.prompt_file_output()  # file extensions, parallel or in-place

            output_dict, new_path = guidedcli.transform_outputs(
                file_array, dir_struct_type, orig_path, output_filetype)

        guidedcli.confirm_choices(orig_path, new_path, output_filetype)

        multiexec.execute_ffmpeg_split(ffmpeg_dir, output_dict, args_array[0], args_array[1])

        if reusing:
            guidedcli.sqlite_update(preset, prunelist, output_dict)
        else:
            guidedcli.sqlite_store(output_dict, orig_path, new_path, input_filetypes, output_filetype, args_array)

        print(colortext("\n!!! MUSIC CONVERSION COMPLETE !!!\n", "purple", style="b"))
    elif output_mode == "--gui":
        gui.main()
    elif output_mode == "--cli":
        print(colortext("not yet implemented, sorry :(", "red"))
        exit()


if __name__ == "__main__":
    main()
