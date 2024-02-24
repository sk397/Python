# Set Data Type
# No duplicate elements 
# Set is fast for lookup, addtion, etc


x= set() # this is a set
s = {4,3,8,5} # This is a set
s2 = {4,6,7,3,8,5} # This is another set
y = {} # An empty sqaure brakers is a dictornary

print(type(x))
print(type(s))
print(type(y))

# Adding an element to a set
s.add(6)
print(s)
#Removing from a set
s.remove(4)
print(s)

#Printing a particular element in a set
#This will give the boolen value of True as the elements are present
print(3 in s)  
print(5 in s2)
print(11 in s2)

#Union of Set
#The Python set union() function returns a set containing all the distinct items 
#from the original declared set as well as all items from the specified sets.
print(s.union(s2))

# Differnece of set
#The difference() method returns a set that contains the difference between two sets.
# Meaning: The returned set contains items that exist only in the first set, and not in both sets.
print(s.difference(s2))


# Intersection of set
#The intersection() method returns a set that contains the similarity between two or more sets. 
#Meaning: The returned set contains only items that exist in both sets, or in all sets if the comparison is done with more than two sets.
print(s.intersection(s2))
