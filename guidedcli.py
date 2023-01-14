# jmelancon
# joseph@jmelancon.com
# 2023

import menuutils
import syscheck
import filetypes
import fileops
import sqlite3
import os
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
    return file_array, music_dir, file_exts


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


def transform_outputs(input_array, output_type, orig_path, format_ext, provided_dir = ""):
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

        if provided_dir == "":
            # get the new directory and add a '/' if nessesary at the end
            print(colortext("\nfor parallel directories, we'll need a new place for output files.", "cyan"))
            print(colortext("directories are created automatically if they don't exist,", "cyan"))
            print(colortext("so be careful that you aren't making any typos.\n", "cyan"))
            new_dir = str(input(colortext("new music dir:\n>>> ", "yellow")))
            print()
        else:
            new_dir = provided_dir
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
    print(colortext("the program is now ready to convert your music.\n", "cyan"))
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
        else:
            print((colortext("\ni won't start until \"yes\" is typed in all caps.", "yellow", style="i")))


def sqlite_import():
    print(colortext("a record of previous conversions was found.", "cyan"))
    print(colortext("\nwould you like to use one of these records?\n", "cyan"))
    do_reuse = str(input(colortext("reuse a record? (y/N)\n>>> ", "yellow")))
    # if it's not 'y' or 'Y', we do not care.
    if do_reuse.lower() == "y":
        conn = sqlite3.connect("conversiondata.db")
        cur = conn.cursor()

        preset_names = []
        res = cur.execute("select name from presets;")
        print(colortext("\nsaved presets:", "cyan"))
        for line in res:
            preset_names.append(line[0])
        for line in preset_names:
            print(colortext("  • {}".format(line), "blue"))
            preset_in_path = cur.execute(f'select input_folder from presets where name="{line}";').fetchone()[0]
            preset_out_path = cur.execute(f'select output_folder from presets where name="{line}";').fetchone()[0]
            preset_ft = cur.execute(f'select output_filetype from presets where name="{line}";').fetchone()[0]
            print(colortext("    • input folder: {}".format(preset_in_path), "blue"))
            print(colortext("    • output folder: {}".format(preset_out_path), "blue"))
            print(colortext("    • output filetype: {}\n".format(preset_ft), "blue"))

        print(colortext("please select a preset to reuse. type the full name.\n", "cyan"))

        while True:
            try:
                selection = str(input(colortext("which preset to use?\n>>> ", "yellow")))
                if selection not in preset_names:
                    raise ValueError
                break
            except ValueError:
                print(colortext("\ninvalid preset name. please try again.\n", "red"))

        print(colortext("\nreading music changes. hold tight, this may take some time.", "cyan"))

        # get file listings
        input_files_import = cur.execute(
            f'select input_path, input_hash from files where preset_name="{selection}";').fetchall()
        output_files_import = cur.execute(
            f'select output_path, output_hash from files where preset_name="{selection}";').fetchall()
        input_output_import = cur.execute(
            f'select input_path, output_path from files where preset_name="{selection}";').fetchall()

        # used to modify sqlite later
        cutfiles = []
        recfiles = []

        # all the cases for how files can end up
        new_files = []                              # New input, no output
        in_ok_out_ok_files = []                     # OK input, OK output
        in_ok_out_upd_files = []                    # OK input, updated output
        in_ok_out_gone_files = []                   # OK input, no output
        in_upd_out_ok_files = []                    # Updated input, OK output
        in_upd_out_upd_files = []                   # Updated input, updated output
        in_upd_out_gone_files = []                  # Updated input, no output
        in_gone_out_unnacounted_files = []                   # No input, no output. Variable only used temporarily.

        # get files as a dict with their hashes
        input_files = {a[0]:a[1] for a in input_files_import}
        output_files = {a[0]: a[1] for a in output_files_import}

        # this dict is used to find the relevant output for an input
        iodict = {a[0]:a[1] for a in input_output_import}

        # get preset details
        input_path, output_path, output_filetype, args = cur.execute(f'select input_folder, output_folder, output_filetype, output_args from presets where name="{selection}";').fetchall()[0]
        input_filetypes = cur.execute(f'select input_filetypes from presets where name="{selection}";').fetchone()[0].split(",")

        if input_filetypes == ['all']:
            # Need to process filetypes so files can actually be found
            input_filetypes = []
            for each in filetypes.format_dict_music.values():
                input_filetypes += each

        current_files = fileops.find_files(input_path, input_filetypes)

        for file in current_files:
            if file in input_files.keys():
                # File Exists
                file_hash = fileops.get_hash(file)

                if file_hash == input_files[file] and os.path.exists(iodict[file]):
                    # File is unchanged and output file still exists
                    outfile_hash = fileops.get_hash(iodict[file])
                    if output_files[iodict[file]] == outfile_hash:
                        in_ok_out_ok_files.append(file)
                    else:
                        in_ok_out_upd_files.append(file)

                elif file_hash == input_files[file]:
                    # File is unchanged but output file is missing
                    in_ok_out_gone_files.append(file)

                elif os.path.exists(iodict[file]):
                    # File is changed, output exists
                    outfile_hash = fileops.get_hash(iodict[file])
                    if output_files[iodict[file]] == outfile_hash:
                        in_upd_out_ok_files.append(file)
                    else:
                        in_upd_out_upd_files.append(file)
                else:
                    # File is changed, output missing
                    in_upd_out_gone_files.append(file)
            else:
                new_files.append(file)

        combined_files = in_upd_out_ok_files + in_upd_out_upd_files + \
                         new_files + in_ok_out_ok_files + in_ok_out_upd_files + \
                         in_ok_out_gone_files

        for key in input_files.keys():
            if key not in combined_files:
                in_gone_out_unnacounted_files.append(key)

        # moar file sorting
        in_gone_out_upd_files = []      # Missing input, updated output
        in_gone_out_ok_files = []       # Missing input, OK output
        in_gone_out_gone_files = []     # Missing input, missing output

        for file in in_gone_out_unnacounted_files:
            if os.path.exists(iodict[file]):
                outfile_hash = fileops.get_hash(iodict[file])
                if output_files[iodict[file]] == outfile_hash:
                    in_gone_out_ok_files.append(file)
                else:
                    in_gone_out_upd_files.append(file)
            else:
                in_gone_out_gone_files.append(file)

        print(colortext("\ninput file status report:", "cyan"))
        print(colortext(f"  • {len(in_ok_out_ok_files)} unchanged files w/ unchanged output", "blue"))
        print(colortext(f"  • {len(in_ok_out_upd_files)} unchanged files w/ changed output", "blue"))
        print(colortext(f"  • {len(in_ok_out_gone_files)} unchanged files w/ missing output", "blue"))
        print(colortext(f"\n  • {len(in_upd_out_ok_files)} changed files w/ unchanged output", "blue"))
        print(colortext(f"  • {len(in_upd_out_upd_files)} changed files w/ changed output", "blue"))
        print(colortext(f"  • {len(in_upd_out_gone_files)} changed files w/ missing output", "blue"))
        print(colortext(f"\n  • {len(in_gone_out_ok_files)} missing files w/ unchanged output", "blue"))
        print(colortext(f"  • {len(in_gone_out_upd_files)} missing files w/ changed output", "blue"))
        print(colortext(f"  • {len(in_gone_out_gone_files)} missing files w/ missing output", "blue"))
        print(colortext(f"\n  • {len(new_files)} new files", "blue"))

        # sqlite prep
        cutfiles += in_gone_out_gone_files

        if len(in_ok_out_upd_files) > 0:
            print(colortext("\nwould you like to recreate files with unchanged inputs and changed output files or skip them?\n", "cyan"))
            do_delete = str(input(colortext("recreate or skip? (r/S)\n>>> ", "yellow")))
            # if it's not 'r' or 'R', we do not care.
            if do_reuse.lower() == "r":
                for file in in_ok_out_upd_files:
                    if os.path.exists(iodict[file]):
                        os.remove(iodict[file])
                new_files += in_ok_out_upd_files
                recfiles += in_ok_out_upd_files

        if len(in_ok_out_gone_files) > 0:
            print(colortext(
                "\nwould you like to recreate files with unchanged inputs and missing output files or skip them?\n",
                "cyan"))
            do_recreate = str(input(colortext("recreate or skip? (r/S)\n>>> ", "yellow")))
            # if it's not 's' or 'S', we do not care.
            if do_recreate.lower() == "r":
                for file in in_ok_out_gone_files:
                    if os.path.exists(iodict[file]):
                        os.remove(iodict[file])
                new_files += in_ok_out_gone_files
                recfiles += in_ok_out_gone_files

        if len(in_upd_out_upd_files) > 0:
            print(colortext(
                "\nwould you like to recreate files with changed inputs and changed output files or skip them?\n",
                "cyan"))
            do_recreate = str(input(colortext("recreate or skip? (r/S)\n>>> ", "yellow")))
            if do_recreate.lower() == "r":
                for file in in_upd_out_upd_files:
                    if os.path.exists(iodict[file]):
                        os.remove(iodict[file])
                new_files += in_upd_out_upd_files
                recfiles += in_upd_out_upd_files

        if len(in_upd_out_ok_files) > 0:
            print(colortext(
                "\nwould you like to recreate files with changed inputs and unchanged output files or skip them?\n",
                "cyan"))
            do_recreate = str(input(colortext("recreate or skip? (r/S)\n>>> ", "yellow")))
            if do_recreate.lower() == "r":
                for file in in_upd_out_ok_files:
                    if os.path.exists(iodict[file]):
                        os.remove(iodict[file])
                new_files += in_upd_out_ok_files
                recfiles += in_upd_out_upd_files

        if len(in_upd_out_gone_files) > 0:
            new_files += in_upd_out_gone_files
            recfiles += in_upd_out_gone_files

        if len(in_gone_out_upd_files + in_gone_out_ok_files) > 0:
            print(colortext(
                "\nwould you like to keep or delete output files with missing inputs?\n",
                "cyan"))
            do_recreate = str(input(colortext("keep or delete? (K/d)\n>>> ", "yellow")))
            if do_recreate.lower() == "d":
                for file in in_gone_out_upd_files + in_gone_out_ok_files:
                    if os.path.exists(iodict[file]):
                        os.remove(iodict[file])
                cutfiles += in_gone_out_upd_files + in_gone_out_ok_files
        dir_type = 1

        if "/".join(list(iodict.keys())[0].split("/")[:-1]) == "/".join(iodict[list(iodict.keys())[0]].split("/")[:-1]):
            dir_type = 2

        if "-ab" in args:
            args_array = [args, ""]
        else:
            args_array = [args, syscheck.find_ffprobe()]

        output_dict, ignore = transform_outputs(new_files, dir_type, input_path, output_filetype, output_path)

        # sqlite update ops (post conversion)

        prunelist = dict()
        for file in cutfiles:
            prunelist[file] = 'c'
        for file in new_files:
            prunelist[file] = 'a'
        for file in recfiles:
            prunelist[file] = 'r'

        if len(new_files) + len(recfiles) == 0:
            print(colortext("\nnothing to do! all files are in order :)\n\nprogram will exit. goodbye!\n", "cyan"))
            exit()
        print()
        return input_path, output_path, input_filetypes, output_filetype, output_dict, args_array, selection, prunelist

    else:
        return None


def sqlite_store(files_dict, orig_path, new_path, input_filetypes, output_filetype, args_array):
    print(colortext("\nwould you like to keep a record of the files you've converted?", "cyan"))
    print(colortext("you'll be able to skip converting unchanged files next time you use the same options.\n", "cyan"))
    do_store = str(input(colortext("keep record? (y/N)\n>>> ", "yellow")))
    # if it's not 'y' or 'Y', we do not care.
    if do_store.lower() == "y":
        conn = sqlite3.connect("conversiondata.db")
        cur = conn.cursor()

        tables = []
        res = cur.execute("select name from sqlite_master;")
        for line in res:
            tables.append(line[0])

        if "files" not in tables:
            joiner = " TEXT not null, "
            colnames = ["preset_name", "input_path", "input_hash", "output_path", "output_hash"]
            cols = joiner.join(colnames) + " TEXT not null"
            cur.execute(f'create table files ({cols});')
            conn.commit()

        if "presets" not in tables:
            joiner = " TEXT not null, "
            colnames = ["name", "input_folder", "input_filetypes", "output_folder", "output_filetype", "output_args"]
            cols =  joiner.join(colnames) + " TEXT not null"
            cur.execute(f'create table presets ({cols});')
            conn.commit()

        preset_names = []
        res = cur.execute("select name from presets;")
        for line in res:
            preset_names.append(line[0])

        while True:
            try:
                preset_name = str(input(colortext("preset name\n>>> ", "yellow")))
                if preset_name in preset_names:
                    raise FileExistsError
                if not preset_name.isalpha():
                    raise ValueError
                break
            except ValueError:
                print(colortext("\nthere was an issue with your input. please try again.\n", "red"))
            except FileExistsError:
                print(colortext("\npreset name already used. please try another name.\n", "red"))

        for key in files_dict.keys():
            # get input hash
            input_hash = fileops.get_hash(key)

            # get output hash
            output_hash = fileops.get_hash(files_dict[key])

            # join values into part of the sql statement
            values = '"' + '", "'.join([preset_name, key, input_hash, files_dict[key], output_hash]) + '"'

            # execute statement
            cur.execute(f'insert into files values({values});')

        # write preset
        joined_ift = ",".join(input_filetypes)
        values = '"' + '", "'.join([preset_name, orig_path, joined_ift, new_path, output_filetype, args_array[0]]) + '"'
        cur.execute(f'insert into presets values({values});')

        # commit and close
        conn.commit()
        conn.close()


def sqlite_update(preset, prunelist, output_dict):
    conn = sqlite3.connect("conversiondata.db")
    cur = conn.cursor()

    for file in prunelist.keys():
        if prunelist[file] != 'a':
            cur.execute(f'delete from files where input_path = "{file}" AND preset_name = "{preset}"')
            conn.commit()
        if prunelist[file] != 'c':
            in_hash = fileops.get_hash(file)
            out_hash = fileops.get_hash(output_dict[file])
            values = '"' + '", "'.join([preset, file, in_hash, output_dict[file], out_hash]) + '"'
            cur.execute(f'insert into files values({values});')
    conn.commit()
    conn.close()
