# jmelancon
# joseph@jmelancon.com
# 2022

'''get all music files in a directory and convert them via ffmpeg'''

import os
import sys

import syscheck
import fileops
import guidedcli
import gui


def execute_ffmpeg(ffmpeg_dir, io_dict, args):
    '''run ffmpeg'''
    # special case for windows because it is annoying
    # they really like their backlashes and quotes around spaces
    # so the path has to be doctored before we run ffmpeg_dir
    if syscheck.platform == "win32":
        ffmpeg_dir = fileops.prep_dir_win(ffmpeg_dir, False)
    # so for each key in the input/output dictionary, which will be an input,
    # we will use the key (input) to get the value (output), then splice that
    # all into a command string to run via ffmpeg on *nix systems
    for input_dir in io_dict.keys():
        # check if directories exist first!!!
        # see fileops.missing_dir_test_nix()
        output_dir = io_dict[input_dir]
        fileops.missing_dir_test(output_dir)
        # {ffmpeg} -i "{input}" {arguments}"{output}"
        # note that the arguments string has a space at the end by default
        if syscheck.platform == "linux" or syscheck.platform == "unix":
            command = str('"{}" -i "{}" {}"{}"'.format(
                ffmpeg_dir, input_dir, args, io_dict[input_dir]))
        else:
            command = str('{} -i "{}" {}"{}"'.format(
                ffmpeg_dir, fileops.prep_dir_win(input_dir, False), args,
                fileops.prep_dir_win(io_dict[input_dir], False)))
        # moment of truth
        print(command)
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
        print("no arguments passed, assuming guided cli...")
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
        ffmpeg_dir = syscheck.find_ffmpeg()

        file_array_pkg = guidedcli.prompt_file_inputs()  # needs to be unpacked
        # array of files that needs to be converted
        file_array = file_array_pkg[0]
        orig_path = file_array_pkg[1]  # path that we asked the user for

        args = guidedcli.prompt_for_args()  # output args. bitrate, retain art

        output_options_pkg = guidedcli.prompt_file_output()  # get output opts
        format_ext = output_options_pkg[0]  # file extensions
        dir_struct_type = output_options_pkg[1]  # parallel or in-place

        output_dict = guidedcli.transform_outputs(
            file_array, dir_struct_type, orig_path, format_ext)

        execute_ffmpeg(ffmpeg_dir, output_dict, args)
    elif output_mode == "--gui":
        gui.main()
    elif output_mode == "--cli":
        print("not yet implemented, sorry :(")
        exit()


if __name__ == "__main__":
    main()
