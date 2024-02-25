
import sys
import json
import clipboard


SAVED_DATA = "clipboard.json"

# Function to create a JSON file and read JSON File
# we are passing the filepath to the function and this is where we will save our file
# using an open method to open the exiting file im the write mode (w) amnd overwrite it or create a new file in write mode
# as f : this means we will store whatever we will do with the new or overwritten file
# then we use the dump function to dump the data into file f, json file
def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


# Reading the json file and return the json data
# We will try to load the file, if it does not exists, we will return an empty dictonary     
def load_data(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data
    except: 
        return {}


#creating static dummy data - keep below 2 lines commented
#name of file is test.json and data is a key value pair
# save_items("test.json", {"key": "value"})

if len(sys.argv) == 2 :
    command = sys.argv[1]
    data = load_data(SAVED_DATA) #This will give a python dictonary with available items in the file

    if command == "save":
        key = input("Enter a key")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data Saved")

    # We will ask the user a key,if available we return the value else return error
    elif command == "load":
        key = input("Enter a key")
        if key in data:
            clipboard.copy(data[key])
            print("Data Was copied to clipbaord")
        else:
            print("key does not exist")
        print("load")

    # This should list all the keys and values
    elif command == "list":
        print(data)
    else: 
        print("unknown command")
else:
    print("Please pass excatly one command")



