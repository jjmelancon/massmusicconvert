# jmelancon
# joseph@jmelancon.com
# 2023

from colors import colortext

def printArray(print_array):
    '''print long messages stored in arrays'''
    # For each line within the array do the following:
    for line in print_array:
        print(line)                     # Print the line!


def integer_selection(lowest_selection, highest_selection):
    '''determine if a user-provided input is usable for the program'''
    # do this forever or until we break:
    while 1 == 1:
        # try to do these code blocks. if there's an issue, go to except
        try:
            # prompt for a number.
            selection = input(colortext("which one?\n>>> ", "yellow"))
            # if the number is outside of the given range, do this:
            if not lowest_selection <= int(selection) <= highest_selection:
                # tell Python there's an issue with the value
                raise ValueError
            # return the selection if nothing bad happens, break the loop.
            return int(selection)
        # if there was a problem with values, give this error and repeat.
        except ValueError:
            print(colortext("\nsorry, but that doesn't seem to be an option.", "red"))
            print(colortext("please input a whole number within the above range.\n", "red"))
