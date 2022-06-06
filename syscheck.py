# jmelancon
# joseph@jmelancon.com
# 2022

'''verify ffmpeg location and platform compatibility'''

import os
import sys
import fileops
from colors import colortext


platform = sys.platform


def specify_ffmpeg():
    '''ask the user where their ffmpeg/ffprobe install is'''
    # start a loop because the user may input a bad/nonexistent file location
    while 1 == 1:
        # try/except for if a bad file path is supplied
        try:
            # ask for the path
            f_d = str(input(colortext("please type binary's directory or 'quit'\n>>> ", "yellow", style="n")))
            # if a user realizes they don't have ffmpeg, they can just leave
            # we'll test this first because a user may have a file called quit
            if f_d.lower() == "quit":
                print(colortext("\ngoodbye!", "purple", style="b"))
                exit()
            # os.path.exists is able to check if this is a real location
            elif fileops.check_spaces(f_d) and platform == "win32":
                raise Exception(colortext("sorry, binary's path can't have spaces.", "red"))
            elif os.path.exists(f_d):
                print(colortext("\nok! using specified binary.\n", "green"))
                return f_d
            # if neither of these are correct, we didn't find a file.
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            print(colortext("that is not an existing file.", "red"))
            print(colortext("please specify a path to a valid binary.\n", "red"))


def find_ffmpeg():
    '''reports if the system has ffmpeg installed'''
    # add windows support soon(tm)
    # mac support is going to be flaky until everything else is done
    # linux support is my main focus as it's my main os

    win_loc = "c:/ffmpeg/bin/ffmpeg.exe"
    lin_loc = "/bin/ffmpeg"

    # this case is the easiest. ffmpeg at default location on linux.
    if platform == "linux" and os.path.exists(lin_loc):
        print(colortext("found ffmpeg install at /bin/ffmpeg\n", "green", style="i"))
        return lin_loc

    # this is harder. windows uses non standard path separators,
    # so windows will be a pain in my figurative rear end to
    # implement. stay tuned.
    # just exit so i don't have to fix it now.
    elif sys.platform == "win32" and os.path.exists(win_loc):
        print(colortext("!! windows is in preliminary support, continuing...", "yellow", style="b"))
        print(colortext("found ffmpeg install at {}\n".format(win_loc), "green", style="i"))
        return win_loc

    # run this if we can't find ffmpeg for windows!
    elif platform == "win32":
        print(colortext("!! windows is in preliminary support, continuing...", "yellow", style="b"))
        print(colortext("!! i did not find ffmpeg on your system.", "red", style="b"))
        print(colortext("please specify ffmpeg location", "yellow"))
        print(colortext("ffmpeg's path cannot have spaces. refrain from doing that.", "yellow"))
        print(colortext("use '/' instead of '\\' and start with 'c:/' or otherwise!", "yellow"))
        return specify_ffmpeg()

    # darwin is the codename for apple's macos kernel.
    # thanks to macos being unix, the linux commands in this script
    # should just work(tm) on macos.
    # todo: add ffmpeg default install location for mac
    elif platform == "darwin":
        print(colortext("!! i have not yet tested macos!", "yellow", style="b"))
        print(colortext("please specify ffmpeg location", "yellow"))
        return specify_ffmpeg()

    # everyone's linux distro is a little different,
    # so if the platform is linux and ffmpeg isn't in /bin/,
    # we'll ask the user.
    elif sys.platform == "linux":
        print(colortext("!! i did not find ffmpeg on your system.", "red", style="b"))
        print(colortext("please specify ffmpeg location", "yellow"))
        return specify_ffmpeg()

    # i only plan on doing operating systems on a whitelist basis,
    # so if the above fail, just exit.
    else:
        print(colortext("!! sorry, your platform is not supported by this script.", "red", style="b"))
        exit()

def find_ffprobe():
    '''reports if the system has ffprobe installed'''
    # add windows support soon(tm)
    # mac support is going to be flaky until everything else is done
    # linux support is my main focus as it's my main os

    win_loc = "c:/ffmpeg/bin/ffprobe.exe"
    lin_loc = "/bin/ffprobe"

    # this case is the easiest. ffmpeg at default location on linux.
    if platform == "linux" and os.path.exists(lin_loc):
        # print(colortext("\nfound ffprobe install at /bin/ffprobe\n", "green", style="i"))
        return lin_loc

    # this is harder. windows uses non standard path separators,
    # so windows will be a pain in my figurative rear end to
    # implement. stay tuned.
    # just exit so i don't have to fix it now.
    elif sys.platform == "win32" and os.path.exists(win_loc):
        # print(colortext("\nfound ffprobe install at {}\n".format(win_loc), "green", style="i"))
        return win_loc

    # run this if we can't find ffmpeg for windows!
    elif platform == "win32":
        print(colortext("\n!! i did not find ffprobe on your system.", "red", style="b"))
        print(colortext("!! i need this in order to properly retain the old bitrate.", "red", style="b"))
        print(colortext("please specify ffmpeg location", "yellow"))
        return specify_ffmpeg()

    # darwin is the codename for apple's macos kernel.
    # thanks to macos being unix, the linux commands in this script
    # should just work(tm) on macos.
    # todo: add ffmpeg default install location for mac
    elif platform == "darwin":
        print(colortext("\n!! i have not yet tested macos!", "yellow", style="b"))
        print(colortext("please specify ffprobe location", "yellow"))
        print(colortext("this is needed to retain source bitrates.", "yellow"))
        return specify_ffmpeg()

    # everyone's linux distro is a little different,
    # so if the platform is linux and ffmpeg isn't in /bin/,
    # we'll ask the user.
    elif sys.platform == "linux":
        print(colortext("\n!! i did not find ffprobe on your system.", "red", style="b"))
        print(colortext("please specify ffprobe location", "yellow"))
        print(colortext("this is needed to retain source bitrates.", "yellow"))
        return specify_ffmpeg()
