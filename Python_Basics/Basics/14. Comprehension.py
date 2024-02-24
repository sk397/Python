# Comprehension in Python

x = [x for x in range(5)]
print(x)

x = [x+5 for x in range(5)]
print(x)

x = [x%5 for x in range(5)]
print(x)

#Loop inside Loop
x = [[4 for x in range(10)] for x in range (5)]
print(x)

# More complex stuff
x = [[i for i in range(60) if i % 5 ==0]]
print(x)

# making dict out of above
x = {i:0 for i in range(60) if i % 5 ==0}
print(x)

# making a set out of above
x = {i for i in range(60) if i % 5 ==0}
print(x)

# making a tuple out of above
x = tuple(i for i in range(60) if i % 5 == 0)
print(x)