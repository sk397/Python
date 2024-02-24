# Slice operator is simply with square brackets and cloons [::]

x = [0,1,2,3,4,5,6,7,8]
y = ['hi', 'hlo', 'okay','bye','sure']
s = "hello"

#[start:stop:step]
sliced = x[0:4:2]
# in the X, we start at 0, stop a 4 but not inclue it, and increment by 2
# So we get 0,2

print(sliced)

# Start at 0 go till 4 but not inclue it
abc=x[:4]
print(abc)

# Start at 4 go till the end of x list
xyz=x[4:]
print(xyz)

# Reverse a list
pqr=x[::-1] # Reverse skip by 1
pqr=x[::-2] # Reverse skip by 2
print(pqr)


#Using slice on a tuple
atuple = (1,2,3,4,5,6,9)[::2]
print(atuple)




