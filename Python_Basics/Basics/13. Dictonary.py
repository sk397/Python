# Dictonary is a key value pair [Hashmap in Java]
#Very fast to add key and value 

x= {'key' : 4}
x2= {'key2' : 5}
print(x['key']) # This will print the value of this key
print(x2['key2']) # This will print the value of this key

#Adding a new key
x2['key3'] = 7
print(x2)
print(x2['key3'])

#Adding a new key and value
x2[2] = [5,6,7,8]
print(x2)

#Chekcing if a key is in dictornary
print(2 in x2)
print(x2.values())

#priting a list of keys
print(list(x.keys()))
print(list(x2.keys()))
print((x2.keys())) # without list keyword the dict_keys keyword is appended

# Listing the values
print(list(x2.values()))


# Deleting values in dict
del x2[2]
print(x2)

#iterating over a dict
for key , value in x2.items():
    print(key, value)

#same as above but we are getting the values of key in the print statement
for key in x2:
    print(key, x2[key])

