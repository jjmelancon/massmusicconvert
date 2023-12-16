---
layout: page
title: The Preview Branch
desc: Details on the preview branch for massmusicconvert.
permalink: /previewbranch/
importance: 3
---

# The Preview Branch  

## The Why  

I seldom update my code. I find myself creating things and not getting around to completing them. 
For this reason, the `preview` branch exists. This branch will contain new features that I intent to 
merge into the `main` branch at some point. Often, this branch will be more unstable but will be an 
overall more complete version of the program.

## What's On the Preview Branch?

Currently, one big change. The preview branch now implements SQLite in order to store records of your
conversion history. With this, one can transcode an ever-expanding library without having to re-transcode
every time. It'll save your choices for format, bitrate, and file structure. 

## The Bugs

On the branch at this time, there's a few bugs I can remeber off the top of my head.

 - The database is stored in the working directory. This means you must be in the same directory
   as `musicconvert.py` when running or else the file will save... somewhere unexpected. I might fix
   this behavior? Maybe?

 - The keyboard locks up after transcode for reasons unknown to me. It likely has something to do 
   with how processes are spawned. The fix for this seems to be running `stty sane` immediately after 
   the multiprocessing queue is emptied. Again, maybe I'll implement this? I also need to do more testing
   though. I've only verified that this fixes the issue on Linux over whatever terminal emulator is implemented 
   in the Proxmox web interface. I'm not sure if the issue is present on Windows.

 - The program checks for external modifications by using a checksum, MD5 if I'm not mistaken. This takes time to 
   generate checksums though and ideally I'd like to minimize this time. It may be worthwhile to see if there's 
   a different way to do checksums. Modification date and time may be a viable option, but I'd still lean towards 
   the former method.

## Aquiring the Preview Branch

Use git to clone the branch. I usually don't push code unless it's working, trust me bro.

