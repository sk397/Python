import sys
import json
import clipboard

# This is how you show the copied data to clipboard
data = clipboard.paste()
print(data)

# Used to copy to clipboard
clipboard.copy("abc")

# Sys module #argv will give all the command line aruguments  to you
print(sys.argv)

# If we just need the 1st index of the passed argumenets
# print(sys.argv[2])

#here we are chking if the passed Argument is equal to 2 
# one would be the python keyword and other the argument we pass
if len(sys.argv) == 2 :
    command = sys.argv[1]

    if command == "save":
        print("save")
    elif command == "load":
        print("load")
    elif command == "list":
        print("list")
    else: 
        print("unknown command")
else:
    print("Please pass excatly one command")

