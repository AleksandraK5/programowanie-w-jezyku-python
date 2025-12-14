class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average_marks = sum(self.marks) / len(self.marks)
        return average_marks > 50


student1 = Student("Agnieszka Nowak", [80, 70, 90])
student2 = Student("Adam Roman", [30, 20, 50])
print(student1.is_passed())
print(student2.is_passed())
