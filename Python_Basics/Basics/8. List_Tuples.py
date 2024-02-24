# List

x = [4, True, "Hello"]  # List has 3 itmes
y="h1" # This string has 2 letters
print(len(x), len(y))

# Extending the list
x.extend([4,5,6,7,8,9])
print(x)

# Popping the last element
x=[4, True,'hey']
print(x.pop()) # This will give the popped element
print(x) # Print the list after the element is popped
print(x[-1]) # This will give the elements after the popped list

# Adding the elemet to the 0th index in the list
x[0] = 'Hello'
print(x)

# Appending the value in the list
#List is a Collection of changable collection of items
z=[8,7,5,7]
z.append(9)
print(z)
print(z[0])
print(z[-1])


# Tuples #Collection of unchagable collection of items
mytuple = ("apple", "banana", "cherry")
print(mytuple)
print(len(mytuple))


