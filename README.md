# massmusicconvert

## wip!

massmusicconvert is a Python3 script that recursively scans a directory in an effort to find music files. this list is passed to ffmpeg for conversion. i plan on extending this project to support more media files like videos in the future, as well as considering adding support for ripping music. this project is gplv3, use it however you would like within the terms of the license.

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
