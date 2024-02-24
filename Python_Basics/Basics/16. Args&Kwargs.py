
def func(x):
    def func2():
        print(x)

    return func2

print(func(3)) # This prints and shows that gere is a function in the fucntion

# here we are printing the func 2 as func(2) and then we are calling it by adding the ()
# This reurns the value of x and then none as there is nothing to return for func2
print(func(3)())  



#Args & Kwrgs in Python
def func (*args, **kwargs):
    pass

x = [1,23,23456,5566]
print(*x) #Prints all individually
print(x) #prints the list


#For a list or tuple
def func(x,y):
    print(x,y)
pairs = [(1,2), (3,4)]
for pair in pairs:
    func(*pair)


# For Dictonary
def func(x,y):
    print(x,y)
func(**{'x':2, 'y':5})


#*args means argumanets and **kwargs meanes keybaord aruguments
def func(*args, **kwargs):
    print(args,kwargs)

func(1,2,3,4,5, one=1, two=2)
# Args (Argument) will print the individual elemets and 
# kwargs( keyword arguments) will print the keyword elements
