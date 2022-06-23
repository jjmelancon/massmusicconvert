---
layout: page
title: Home
permalink: /
---
# massmusicconvert

massmusicconvert is a Python3 script that aims to convert a folder full of music to a different format of the user's choice. The script works by recursively scanning a directory in an effort to find music files, then passing the files one by one to FFmpeg for conversion. This project is AGPLv3, use it however you would like within the terms of the license.  

## usage  

To get started, head over to the [Program Usage]({% post_url usage %}) page.

## supported platforms:

**Linux**: Yes. Tested on Arch Linux and Fedora 35 with Python 3.10.1, both running kernel 5.16  
**MacOS**: Maybe. I do not own a Mac and am too lazy to make a virtual machine at this time. All Linux commands should interface properly with their Unix counterparts, but don't count on any formal testing yet.  
**Windows**: ***Kinda***. Windows uses a vastly different directory structure than a Unix or Linux type system, using C:\ as root as well as using backslashes instead of forward slashes like a sane operating system. Thus, separate functions must be made to convert python input to an output that Win32's CMD can understand. I've made functions to handle these specific issues, however no spaces can be in the FFmpeg directory path as a result of issues with getting Win32's CMD to interpret spaces in directories properly. No other issues have manifested at this time.

## dependencies:

**Linux**: Python3, FFmpeg. Install FFmpeg to /bin/ffmpeg or manually specify the path to your FFmpeg directory.  
**MacOS**: Python3, FFmpeg. You must manually specify where FFmpeg is located.  
**Windows**: Python3, FFmpeg. Install FFmpeg to C:\ffmpeg\bin\ffmpeg.exe or manually specify the path to your FFmpeg directory.

## running:

If you want to run this code, good luck lol. Your best bet will be to use a release version on a Linux distro. I'm still working on the code, so consider everything in the main branch broken until this program reaches a full release, meaning I've accomplished everything in the todo section.

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

### need to do:

Verify MacOS compatibility  
Figure out bitrate selection issues  
Build proper GUI (Tkinter?)  
Implement more features  
Standalone Windows executable  
Documentation  

### ongoing goals:

Keep code clean and commented  
Simplify convoluted code  
Adhere to PEP8 as best as possible  
