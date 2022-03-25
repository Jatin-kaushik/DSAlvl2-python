class Student:
    def __init__(self, name = "None" , rollno=0):
        self.name = name
        self.rollno = rollno
    
    def display(self):
        print("Student name is " + self.name + " and his rollno is " + str(self.rollno))

a = Student()
a.display()
a.name = "jatin"
a.rollno = 420
a.display()

b = Student("Ramu", 421)
b.display()