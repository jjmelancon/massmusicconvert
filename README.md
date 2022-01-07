# massmusicconvert

## this project is a work in progress!

### massmusicconvert is a Python3 script that recursively scans a directory in an effort to find music files. this list is passed to ffmpeg for conversion. i'm very *lightly* considering adding support for scraping metadata. this project is gplv3, use it however you would like within the terms of the license.  

## documentation:

there is no documentation at this time, hmu if you have any questions.  

## supported platforms:

linux: yes. tested on Arch Linux 5.15 with Python 3.10.1  
macos: maybe. i do not own a mac and am too lazy to make a virtual machine at this time. all linux commands should interface properly with their unix counterparts, but don't count on any formal testing yet.  
windows: **no**. windows uses a vastly different directory structure than a unix or linux type system, using C:\ as root as well as using backslashes instead of forward slashes like a sane operating system. this is next on the chopping block, but it's gonna be a bumpy road.  

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

get it working on windows  
verify macos compatibility  
figure out bitrate selection issues  
create command line argument interface  
build proper gui (tkinter?)  
implement features  
standalone windows executable  
documentation  

### ongoing goals:

keep code clean and commented  
simplify convoluted code  
adhere to pep8 as best as possible  
