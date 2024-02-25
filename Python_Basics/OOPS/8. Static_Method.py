# Static Methods in Python
# Not chaning methods , they do not have access to an instance
# It cant access anything, its just a simple fucntion
# We can directly use the class and do need to create an instance

class Math:
    @staticmethod
    def add5(x):
        return x + 5
    
    @staticmethod
    def Subract5(x):
        return x - 5
    
    staticmethod
    def pr():
        print("Hello")
    

print(Math.add5(10))
Math.pr()
