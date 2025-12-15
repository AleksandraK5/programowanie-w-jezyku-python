from klasy.Employee import Employee
from klasy.Book import Book
from klasy.Student_2 import Student


class Order:
    def __init__(self, employee: Employee, student: Student,
                 books: Book, order_date: str) -> None:
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return (f'{self.student}\n{self.books}\n'
                f'Order date: {self.order_date}\n{self.employee}\n')
