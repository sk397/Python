# Map and Filter in Python 


#Take every element of x and map the lambda fucntion i to them
x = [1,2,3,45,96,78,8,4,87,56,7,5,556]
mp = map(lambda i: i+2, x) 
# 2 will be added to the element of x and printed in the list form
print(list(mp))


# Filter in Python # Filter out the list based on the lambda function
x = [1,2,3,45,96,78,8,4,87,56,7,5,556]
mp = filter(lambda i: i%2==0, x) 
print(list(mp))

