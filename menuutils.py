# Joseph Melancon
# Waconia RoboCats 4198
# joseph@jmelancon.com, (952)-992-0214
# 2022

# Function to print longer messages stored in arrays. Useful for welcome messages or lists.
def printArray(arrayToPrint):
    # For each line within the array do the following:
    for line in arrayToPrint:
        print(line)                     # Print the line!

# Determine if a user-provided input is usable for the program
def integerSelection(lowestSelection, highestSelection):
    # Do this forever or until we break:
    while 1 == 1:
        # Try to do these code blocks. If there's an issue, go to the except sections
        try:
            # Prompt for a number.
            selection = input("\n!! Please select an operation.\n\n>>> ")
            # If the number is outside of the given range, do this:
            if not lowestSelection <= int(selection) <= highestSelection:
                # Tell Python there's an issue with the value
                raise ValueError
            # Return the selection if nothing bad happens, break the loop.
            return int(selection)
        # If there was a problem with values, give this error and repeat.
        except ValueError:
            print("\n!! I'm sorry, but that doesn't seem to be an option.\n!! Can I have a whole number within the above range?\n")
        # If there was any other problem, give this error and repeat.
        except:
            print("\n!! I'm sorry, but there's an issue with the option you provided.\n!! Can I have a whole number within the above range?\n")