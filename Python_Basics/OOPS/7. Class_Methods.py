# Function Methods in python

class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    #This method is used to be on the class itself, and not associated with instance
    # So we use cls as it denoes class, unlike we use self for instance
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    # We are referenceing the below class method on the 
    # first method to increment the number of people
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


p1 = Person("Jim")
p2 = Person("Tim")

print(Person.number_of_people_())