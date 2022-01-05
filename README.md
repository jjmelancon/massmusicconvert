# massmusicconvert

## wip!

massmusicconvert is a Python3 script that recursively scans a directory in an effort to find music files. this list is passed to ffmpeg for conversion. i plan on extending this project to support more media files like videos in the future, as well as considering adding support for ripping music. this project is gplv3, use it however you would like.

## task list:

### done:

scan for files
select by file type

### need to do:

check for ffmpeg on at least linux. possibly implement windows support.
either convert alongside (easy), or parallel into a new directory (medium)
actually pass commands to ffmpeg
provide guided and command line interface
