# massmusicconvert

## this project is a work in progress!

### massmusicconvert is a Python3 script that recursively scans a directory in an effort to find music files. this list is passed to ffmpeg for conversion. i'm very *lightly* considering adding support for scraping metadata. this project is gplv3, use it however you would like within the terms of the license.  

## documentation:

there is no documentation at this time, hmu if you have any questions.  

## supported platforms:

##### **linux**: yes. tested on Arch Linux 5.15 with Python 3.10.1  
##### **macos**: maybe. i do not own a mac and am too lazy to make a virtual machine at this time. all linux commands should interface properly with their unix counterparts, but don't count on any formal testing yet.  
##### **windows**: ***probably***. windows uses a vastly different directory structure than a unix or linux type system, using C:\ as root as well as using backslashes instead of forward slashes like a sane operating system. thus, separate functions must be made to convert python input to an output that win32's cmd can understand. i've made functions to handle these specific issues, however no spaces can be in the ffmpeg directory path as a result of issues with getting win32's cmd to interpret spaces in directories properly. no other issues have manifested at this time.

## dependencies:

##### **linux**: python3, ffmpeg. install ffmpeg to /bin/ffmpeg or manually specify the path to your ffmpeg directory.  
##### **macos**: python3, ffmpeg. you must manually specify where ffmpeg is located.  
##### **windows**: python3, ffmpeg. install ffmpeg to c:/ffmpeg/bin/ffmpeg.exe or manually specify the path to your ffmpeg directory.

## task list:

### done:

scan for files  
select by file type  
check for ffmpeg on linux, mac, & windows  
either convert alongside (easy), or parallel into a new directory (medium)  
actually pass commands to ffmpeg  
guided interface  
parallel directory headaches  
probably working as intended on windows  

### need to do:

check ffmpeg directory on win32 for spaces  
verify macos compatibility  
figure out bitrate selection issues  
build proper gui (tkinter?)  
implement more features  
standalone windows executable  
documentation  

### ongoing goals:

keep code clean and commented  
simplify convoluted code  
adhere to pep8 as best as possible  
