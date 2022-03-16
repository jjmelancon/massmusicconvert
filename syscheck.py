# jmelancon
# joseph@jmelancon.com
# 2022

'''verify ffmpeg location and platform compatibility'''

import os
import sys
import fileops


platform = sys.platform


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
            if f_d.lower() == "quit":
                print("goodbye!")
                exit()
            # os.path.exists is able to check if this is a real location
            elif fileops.check_spaces(f_d) and platform == "win32":
                raise Exception("sorry, ffmpeg's path can't have spaces.")
            elif os.path.exists(f_d):
                print("ok! using specified ffmpeg binary.")
                return f_d
            # if neither of these are correct, we didn't find a file.
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            print("that is not an existing file.")
            print("please specify a path or command to an ffmpeg binary.")


def find_ffmpeg():
    '''reports if the system has ffmpeg installed'''
    # add windows support soon(tm)
    # mac support is very tenative at the moment, idk
    # linux support is my main focus as an Arch user btw

    win_loc = "c:/ffmpeg/bin/ffmpeg.exe"
    lin_loc = "/bin/ffmpeg"

    # this case is the easiest. ffmpeg at default location on linux.
    if platform == "linux" and os.path.exists(lin_loc):
        print("found ffmpeg install at /bin/ffmpeg")
        return lin_loc

    # this is harder. windows uses non standard path separators,
    # so windows will be a pain in my figurative rear end to
    # implement. stay tuned.
    # just exit so i don't have to fix it now.
    elif sys.platform == "win32" and os.path.exists(win_loc):
        print("!! windows is in preliminary support, continuing...")
        print("found ffmpeg install at {}".format(win_loc))
        return win_loc

    # run this if we can't find ffmpeg for windows!
    elif platform == "win32":
        print("!! windows is in preliminary support, continuing...")
        print("!! i did not find ffmpeg on your system.")
        print("please specify ffmpeg location or command")
        print("ffmpeg's path cannot have spaces. refrain from doing that.")
        print("use '/' instead of '\\' and start with 'c:/' or otherwise!")
        return specify_ffmpeg()

    # darwin is the codename for apple's macos kernel.
    # thanks to macos being unix, the linux commands in this script
    # should just work(tm) on macos.
    # todo: add ffmpeg default install location for mac
    elif platform == "darwin":
        print("!! i have not yet tested macos!")
        print("please specify ffmpeg location or command")
        return specify_ffmpeg()

    # everyone's linux distro has some odd, nonstandard bs,
    # so if the platform is linux and ffmpeg isn't in /bin/,
    # we'll ask the user.
    elif sys.platform == "linux":
        print("!! i did not find ffmpeg on your system.")
        print("please specify ffmpeg location or command")
        return specify_ffmpeg()

    # i only plan on doing operating systems on a whitelist basis,
    # so if the above fail, just exit.
    else:
        print("sorry, your platform is not supported by this script.")
        exit()
