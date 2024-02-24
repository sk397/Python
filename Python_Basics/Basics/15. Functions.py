# Fucntions in Python

def runfunc():
    print("Run")

def run1func():
    print("Run1")
   
    
runfunc()
run1func()


# Multiply numbers
def Mulfunc(x,y):
    print("run")
    return x*y, x/y # We get the result a Tuple
print(Mulfunc(5,6))


# Get the get the values seperately as well
r1, r2 = Mulfunc(5,6)
print("Hello", r1,r2)