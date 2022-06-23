---
layout: page
title: Program Usage
permalink: /usage/
---
# Program Usage  
As no GUI has been created for massmusicconvert yet, it's only usable from the command line. Thus, I'll explain how to use the program here. It'll be split into two sections, one for Mac and GNU/Linux systems, and one for Windows systems. First, however, I'd like to touch on the general process of how the program works. You don't necessarily need to read through the following section as the script should guide you pretty well, but I'd like to touch on some things that I thought were important to mention.

## Page Contents

* [Explanation of Program Process](#program-flow)
* [Getting Things Running](#getting-things-running)
  * [Windows 10 and 11 Instructions](#windows-10-and-11)
  * [Mac and GNU/Linux Instructions](#gnulinux-and-mac)

## Program Flow
After you start the program, you'll need to get through a few questions before you can convert your music. The flow is as follows:  

1. Find FFmpeg  
    - If FFmpeg isn't found, you will be asked where it is.  
    - If FFmpeg is found, the program will move on.  

2. Music Input  
    1. Specify Music Location  
    2. Specify Music Formats  
        - Here, you can either choose to only select specific formats or just to grab any files recognised as music. I usually just type `all` to do the latter.  
        - If you'd like to make sure your music was grabbed, enter `y` at the next prompt to see a list of all found files. Otherwise, press enter to skip.  

3. Music Conversion Options  
    1. Strip Music Album Art  
        - Responding `y` to this prompt will remove any album art from the converted files. This should only be used if you'd like to cut down on as much space as possible.  
    2. Bitrate  
        - This section is very important if you are looking to cut down on music size. If you'd like to cut down to MP3, for example, you could put in `320` for high quality, `240` for medium quality, and `140` for low quality[^1].  
        - If you'd like to retain a high quality, just enter `0` to use the source content's bitrate. Note that you will need to specify where FFprobe is, a program that should have come with your FFmpeg install. It'll be in the same folder.  

4. Music Output Options  
    1. Specify audio output format  
    2. Specify folder behavior  
        - Parallel means that your music will be in two different folders. For example, you would have one folder that has all your original music files and all of the newly converted files would be dumped into an entirely separate folder.  
            - Upon choosing parallel, you'll need to type in a new folder to put your music in. Beware that the program will make this exact path as you type it, so check for typos before hitting enter.  
        - In-Place means that your music will be put in the same exact folder as before. It'll land right next to the original file with a new name.  

5. Conversion  
    - Sit back and let the computer work. If you plugged everything in correctly, it should start spitting out files into their places.  

## Getting Things Running

Now that you know what this script will ask of you (if you read the [Program Flow](#program-flow) section as I had asked you to), let's talk about getting the script running. Below are instructions for both Windows and *nix based systems. Make sure to follow the instructions for your system as the three operating systems covered in this guide, Windows, MacOS, and GNU/Linux, all have specific needs to run this script.

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

[^1]: These bitrates are deemed high, mid, or low quality in the same manner as how Spotify handles it's quality options.