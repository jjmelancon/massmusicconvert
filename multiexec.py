# jmelancon
# joseph@jmelancon.com
# 2023

'''execute multiple instances of ffmpeg at a time'''

import fileops
import syscheck
import os
import subprocess
from multiprocessing import Pool

def runcommand(command):
    global ran_commands
    global total_commands
    # special windows case :sob:
    if (syscheck.platform == "win32"):
        ffmpeg_process = subprocess.Popen(["powershell.exe", command])
        ffmpeg_process.communicate()
    # sane, non-nt oses
    else:
        subprocess.run(command, shell=True)
    
    

def execute_ffmpeg_split(ffmpeg_dir, io_dict, args, ffprobe_dir):
    '''run ffmpeg across multiple cores'''
    # we need to bake commands for the cores to run.
    # start by making a list to hold these commands.
    command_pool = []

    # prepare ffmpeg dir
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
            bitrate = subprocess.getoutput('"{}" {} "{}"'.format(ffprobe_dir, ffprobe_args, input_dir))[18:-10]
            bitrate_usable = int(bitrate) // 1000
            tmp_args += str("-ab " + str(bitrate_usable) + "k ")
        # {ffmpeg} -i "{input}" {arguments}"{output}"
        if os.path.exists(output_dir):
            # todo: implement better way of handling already existing files
            os.remove(output_dir)
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
        command_pool.append(command)
    pool = Pool()
    a = pool.map(runcommand, command_pool)
