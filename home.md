---
layout: page
title: Home
desc: massmusicconvert is a script to manage converting your whole music library with ease via ffmpeg.
permalink: /
importance: -1
---
# massmusicconvert

massmusicconvert is a Python3 script that aims to convert a folder full of music to a different format of the user's choice. The script works by recursively scanning a directory in an effort to find music files, then passing the files one by one to FFmpeg for conversion. 

## usage  

To get started, head over to the [Program Usage](/usage/) page.

## supported platforms

massmusiconvert has been programmed explicitly for and tested on Windows and GNU/Linux. This project should also work on MacOS as well, though I don't have the means to test it. As I run GNU/Linux on my personal machine, most development will be focused on that specific operating system.

## system requirements

As a helper program, this script only tells other programs what to do. As such, you'll need to download a few things first. The required programs are below:
 * FFmpeg & FFprobe - Handle conversion of music files
   * Windows 10 & 11: Download an executable version from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html) and place the files contained in the archive in `C:\ffmpeg\`. If you can't place the files there, that's alright! You'll just have to tell the program where FFmpeg is later.
   * MacOS: Download an executable version from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html) and place the files contained in the archive anywhere. You'll need to tell the program where these files are located later.
   * GNU/Linux: Install FFmpeg from your distro's package manager. If your distro doesn't have a package manager, I trust that you can figure out how to get FFmpeg working on your own. If FFmpeg isn't in `/bin/`, you'll need to tell the program where it is later.
 * Python3 - Run the program
   * Windows 10 & 11: Install Python from the Microsoft Store.
   * MacOS: Double click `musicconvert.py` in Finder. If Python isn't installed, you'll be prompted to install it.
   * GNU/Linux: Install Python3 from your distro's package manager if it isn't installed already. If your distro doesn't have a package manager, I again trust that you can figure out how to get Python3 working on your own.
