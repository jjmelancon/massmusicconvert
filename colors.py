## joseph melancon
## joseph@jmelancon.com
## from jmelancon/python3modules
## 2023

def colortext(text, textColor, backgroundColor = "", style = "n", highIntensityText = False, highIntensityBG = False):
    colorDict = {
        "black":"0",
        "red":"1",
        "green":"2",
        "yellow":"3",
        "blue":"4",
        "purple":"5",
        "cyan":"6",
        "white":"7"
    }
    styleDict = {
        "n":"0",
        "b":"1",
        "i":"3",
        "u":"4",
    }

    # Hold our color options
    parsedColor = "\033["

    # Handle Styles
    parsedColor += styleDict[style]

    # Handle Text Color
    if highIntensityText:
        parsedColor += ";9" + colorDict[textColor]
    else:
        parsedColor += ";3" + colorDict[textColor]

    # Handle Background Color
    
    if highIntensityBG and backgroundColor != "":
        parsedColor += ";10" + colorDict[backgroundColor] + "m"
    elif backgroundColor != "":
        parsedColor += ";4" + colorDict[backgroundColor] + "m"
    else:
        parsedColor += "m"
        

    #Return Colored String
    return ("{}{}\033[0m".format(parsedColor, text))