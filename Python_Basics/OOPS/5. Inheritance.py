#Inherting from classes

#Main Class
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #Defining a method
    def show(self):
        print(f'I am {self.name} and I am {self.age} years old')

# Inherting the Pet class
class Cat(Pet):
    def speak(self):
        CatSound = "Meow"
        print(f"I am a cat and i make {CatSound}")


class Dog(Pet):
    def speak(self):
        DogSound = "Bark"
        print(f"I am a dog and i make {DogSound}")


# Creating addtional attribuyed for the child class, here we have added the color
class Elephant(Pet):
    def about(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        print(f"Hello my name is {name}, i am {age} years old and i am {color} in color")



# Main Class
p = Pet("Tim", 22)
p.show()

#Inherited Class from main class 
c = Cat("Tom", 30)
c.show()
c.speak() #Method from Child Class

#Inherited Class from main class 
d = Dog("Jerry", 24)
d.show()
d.speak() #Method from Child Class

#Inherited Class from main class with additonal attribute of color
e = Elephant("June", 35)
e.show()
e.about("June", 35, "Black")