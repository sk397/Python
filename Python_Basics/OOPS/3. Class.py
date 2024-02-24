# Class in Python

# Class is a blueprint for an object/ Instance
# inside the Dog class, we have defined an method
class Dog:
    def bark(self):
        print("bark")

    def add_one(self, x):
        return x+1


# Creating a Dog object and using the method inside it   
d = Dog()
print(type(d))
d.bark()

# Since the add one get the return of x+1 , we print the method to see the result
print(d.add_one(5))




# Deifing an Attribute when initilizing the object

class Cat:
    def meow(self):
        print("meow")

    # We are giving the attribute in the __init__ method and delfined an attribute called name 
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        return self.age
        

# defining the atrributes for the cat [name and age]
c1 = Cat("Tim",22)
c2 = Cat("Bill", 10)
c3 = Cat("Tom", 13)

print(c1.name)
print(c2.name)
print(c3.name)

# We will get the name from a method
print(c1.get_name())

# Getting the age of the cat
print(c1.get_age())

# Modfying the age of Cat c1
c1.set_age(10)
print(c1.get_age())








