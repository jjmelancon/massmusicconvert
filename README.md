# massmusicconvert

massmusicconvert is a work-in-progress Python3 script that aims to convert a folder full of music to a different format of the user's choice. The script works by recursively scanning a directory in an effort to find music files, then passing the files one by one to FFmpeg for conversion. This project is GPLv3, use it however you would like within the terms of the license.  

## documentation:

Documentation is available online at https://massmusicconvert.jmelancon.com.

## supported platforms:

**Linux**: Yes. Tested on Arch Linux (Linux 5.15) and Gentoo Linux (Linux 5.18) with Python 3.10.  
**MacOS**: Probably. I do not own a Mac and am too lazy to make a virtual machine at this time. All Linux commands should interface properly with their Unix counterparts, but don't count on any formal testing yet.  
**Windows**: Yes. Tested on Windows 11 with Python 3.10. Separate functions have been created to handle any win32 oddities. The only issue Windows faces is that there may be no spaces in the folders leading up to where ffmpeg is stored. Thus, I recommend putting ffmpeg directly into C:\. See the running section for more information.

## dependencies:

**Linux**: Python3, FFmpeg, (Optional) FFprobe. Install FFmpeg to /bin/ffmpeg or manually specify the path to your FFmpeg directory. The same applies for FFprobe *if* you choose to use the input file's bitrate for the output file.  
**MacOS**: Python3, FFmpeg, (Optional) FFprobe. You must manually specify where FFmpeg is located. The same applies for FFprobe *if* you choose to use the input file's bitrate for the output file.  
**Windows**: Python3, FFmpeg, (Optional). Install FFmpeg to C:\ffmpeg\bin\ffmpeg.exe or manually specify the path to your FFmpeg directory. The same applies for FFprobe *if* you choose to use the input file's bitrate for the output file.    
*Note on FFprobe dependency:* FFprobe is often included with builds of FFmpeg. For Linux users installing FFmpeg from their package manager, FFprobe will likely be installed too. For Windows and MacOS users, FFprobe will likely come in the same zip file as FFmpeg.

## running:

To run the program, see https://massmusicconvert.jmelancon.com/usage/ and scroll down to the relevant section.

## task list:

### done:

Scan for files  
Select by file type  
Check for FFmpeg on Linux, Mac, & Windows  
Either convert alongside (easy), or parallel into a new directory (medium)  
Actually pass commands to FFmpeg  
Guided command line interface  
Parallel directory headaches  
Probably working as intended on Windows  
Check FFmpeg directory on Win32 for spaces  
Multicore processing  
Nice colors  

### need to do:

Verify MacOS compatibility  
Build proper GUI (Tkinter?)  
Implement more features  
Standalone Windows executable  
Improve Documentation  

### ongoing goals:

Keep code clean and commented  
Simplify convoluted code  
Adhere to PEP8 as best as possible  
