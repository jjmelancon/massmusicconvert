---
layout: page
title: Program Usage
desc: Instructions on how to use massmusicconvert through your computer's terminal.
permalink: /usage/
importance: 2
---
# Program Usage  
As no GUI has been created for massmusicconvert yet, it's only usable from the command line. Thus, I'll explain how to use the program here. It'll be split into two sections, one for Mac and GNU/Linux systems, and one for Windows systems. If you'd like a more in-depth explanation of how things work, see [explanation.md](/explanation/) for a closer look into the program. You don't need to read through the following section as the script should guide you pretty well.  

## Page Contents

* [Windows 10 and 11 Instructions](#windows-10-and-11)
* [Mac and GNU/Linux Instructions](#gnulinux-and-mac)

## Getting Things Running

Let's talk about getting the script running. Below are instructions for both Windows and *nix based systems (GNU/Linux and MacOS). Make sure to follow the instructions for your system as the three operating systems covered in this guide, Windows, MacOS, and GNU/Linux, all have specific needs to run this script.

### Windows 10 and 11

#### Prerequesites  
Before running the program, we need to make sure that all required dependencies are installed, those being FFmpeg and Python 3. Windows comes with neither of these, so we'll need to install them if they aren't already. The best way to install Python is to open Powershell either from the start menu or from within Windows Terminal and type `python3 --version`. If Python isn't installed, you'll be brought to the Windows Store to install it. Otherwise, if you get a version number, Python is installed. As for FFmpeg, it can be downloaded from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html). Make sure to grab it in an executable format! Grab the full release build from the applicable "Release Builds" section. As for extracting, you'll need a program that can open 7z archives. I recommend [https://7-zip.org](https://7-zip.org) for this task. Once extracted, rename the folder to "ffmpeg" and place it in `C:\`. If you can't place it there, that's alright! You'll just have to tell the program where ffmpeg is when you start it.  

#### Running the program  
To start, download the latest release from [https://github.com/jmelancon/massmusicconvert/releases](https://github.com/jmelancon/massmusicconvert/releases). You should use the .zip file. Once you have it downloaded, extract it into a folder of your choosing. It'd be a good idea to keep it separate from other files, so don't just drop the files into a folder that already is full of items. After that, you can run the file `musicconvert.py` either by double-clicking it or by running it in Powershell.  

#### Entering directories  
As the program is turning some files into other files, you'll be telling the program where stuff is a lot. That means you'll have to type out exactly where certain things are. When the program asks you to specify a file or folder, you should type in answers like this:  
```c:/Users/username/Music/My Input Files/```  

Some things to note with how this is written:  
    - Nothing is in quotes. If you use quotes in these directories, the script will run into some issues. I am not going to fix this. Just type the path without any quotes.  
    - Nothing special is done to spaces or capitals. They're just typed verbatim as they appear. 
    - Backslashes are NOT used. PLEASE USE FORWARD SLASHES! This choice is made because of how Python handles directories with it's `os` module.  

Here's some examples of entries that WON'T work:  
```
# Quotes
c:/Users/username/Music/"My Input Files"/

# Improper Separator
c:\Users\username\Music\My Input Files\

# Escape Sequences Used on Spaces
c:/Users/username/Music/My\ Input\ Files/
```  

### GNU/Linux and Mac  

#### Prerequesites  
Before running the program, we need to make sure that all required dependencies are installed, those being FFmpeg and Python 3. Most GNU/Linux distros come with Python by default, and FFmpeg can be installed from your distro's package manager in most cases. Mac users will be asked to install Python when running the program, and FFmpeg can be downloaded from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html). Make sure to grab it in an executable format! Put FFmpeg in a memorable spot, because you'll need to type in its location later.  

#### Running the program  
To start, download the latest release from [https://github.com/jmelancon/massmusicconvert/releases](https://github.com/jmelancon/massmusicconvert/releases). You can use either the .zip or .tar.gz file. Once you have it downloaded, extract it into a folder of your choosing. It'd be a good idea to keep it separate from other files, so don't just drop the files into a folder that already is full of items. After that, you can run the file `musicconvert.py` either from your file manager or in the terminal.  

#### Entering directories  
As the program is turning some files into other files, you'll be telling the program where stuff is a lot. That means you'll have to type out exactly where certain things are. When the program asks you to specify a file or folder, you should type in answers like this:  
```/home/username/Music/My Input Files/```  

Some things to note with how this is written:  
    - Nothing is in quotes. If you use quotes in these directories, the script will run into some issues. I am not going to fix this. Just type the path without any quotes.  
    - Nothing special is done to spaces or capitals. They're just typed verbatim as they appear.  

Here's some examples of entries that WON'T work:  
```
# Quotes
/home/username/Music/"My Input Files"/

# Improper Separator
\home\username\Music\My Input Files\

# Escape Sequences Used on Spaces
/home/username/Music/My\ Input\ Files/
```  
