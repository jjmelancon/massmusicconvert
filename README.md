# massmusicconvert

## wip!

massmusicconvert is a Python3 script that recursively scans a directory in an effort to find music files. this list is passed to ffmpeg for conversion. i plan on extending this project to support more media files like videos in the future, as well as *lightly* considering adding support for scraping metadata. this project is gplv3, use it however you would like within the terms of the license.

## supported platforms:

linux: yes. tested on Arch Linux 5.15 with Python 3.10.1  
macos: maybe. i do not own a mac and am too lazy to make a virtual machine at this time. all linux commands should interface properly with their unix counterparts, but don't count on it.  
windows 10/11: no. windows uses a vastly different directory structure than a unix or linux type system, using C:\ as root as well as using backslashes instead of forward slashes like a sane operating system.  

## task list:

### done:

scan for files  
select by file type  
check for ffmpeg on linux  
either convert alongside (easy), or parallel into a new directory (medium)  
actually pass commands to ffmpeg  
guided interface  
parallel directory headaches

### need to do:

figure out bitrate selection issues  
comment my code betterer  
create command line argument interface  
get it working on windows  
build proper gui (tkinter?)  
