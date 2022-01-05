# Joseph Melancon
# joseph@jmelancon.com
# 2022

import os

def findFiles(musicDir):

    dirArray = os.listdir(musicDir)
    fileArray = 

    for each in dirArray:

        newPath = musicDir
        if newPath[-1] != "/":
            newPath += "/"
        newPath += each

        if os.path.isdir(newPath):
            print(newPath + " is a directory! Scanning it too...")
            print(findFiles(newPath))
        
        else:

    return dirArray

def main():
    musicDir = str(input("input music dir.\n>>> "))
    print(findFiles(musicDir))

if __name__ == "__main__":
    main()