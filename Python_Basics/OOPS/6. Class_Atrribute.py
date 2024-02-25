# Class Attributes are only available for a class and not their instance or inherited class

# Number of people is only assocoated with person class and it does
# have any relevenace to the instance / object made out of this class

class person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        person.number_of_people += 1

p1 = person("Tim")
p2 = person("John")

person.number_of_people = 8

# Since the P1 instance does not have the dorect access to the number of person attribute
# but the parent class has, hence we are able to the print result
print(p1.number_of_people)
print(p2.number_of_people)

# Changing the number of people manually
person.number_of_people = 10
print(p1.number_of_people)

# Incrementing the number of people when a new instance is created , we have defined a method in the class
p3 = person("Hey")
print(person.number_of_people)
# We see that now the number of people is incremented by +1 and we get 11



