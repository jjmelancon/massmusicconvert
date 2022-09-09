---
layout: page
title: Program Explanation
permalink: /explanation/
importance: 3
---
# Program Explanation

This page isn't required reading, however, if you'd like more insight on how the program operates without reading the code, any expanded notes I've made on functions that don't warrant their own section have been recorded here.  

## Page Contents

* [Program Flow](#program-flow)

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
        - If you'd like to retain a high quality, just enter `0` to use the source content's bitrate. Note that you may need to specify where FFprobe is, a program that should have come with your FFmpeg install. It'll be in the same folder.  

4. Music Output Options  
    1. Specify audio output format  
    2. Specify folder behavior  
        - Parallel means that your music will be in two different folders. For example, you would have one folder that has all your original music files and all of the newly converted files would be dumped into an entirely separate folder.  
            - Upon choosing parallel, you'll need to type in a new folder to put your music in. Beware that the program will make this exact path as you type it, so check for typos before hitting enter.  
        - In-Place means that your music will be put in the same exact folder as before. It'll land right next to the original file with a new name.  

5. Conversion  
    - Sit back and let the computer work. If you plugged everything in correctly, it should start spitting out files into their places.  

[^1]: These bitrates are deemed high, mid, or low quality in the same manner as how Spotify handles it's quality options.