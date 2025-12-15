class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average_marks = sum(self.marks) / len(self.marks)
        return average_marks > 50
