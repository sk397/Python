class Student:
    def __init__(self,name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 -100

    def get_grade(self):
        return self.grade
    
class course:
    def __init__(self,name, max_students):
        self.name = name
        self.max_students = max_students
        # Creating an empty list of students
        self.students = []
    
    # This student will an instance of the Student class we have defined above
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


s1 = Student("Tim", 19, 95)
s2 = Student("Sai", 29, 75)
s3 = Student("Jimmy", 26, 65)

course = course("Maths", 2)
course.add_student(s1) 
course.add_student(s2) 

# We are gtting the 0th index of the student list
print(course.students[0].name)
print(course.students[0].age)

# Getting the average grade
print(course.get_average_grade())

#Lets add the 3rd studennt to our list, we will get false, as max studentt list is 2
print(course.add_student(s3))

