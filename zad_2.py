from klasy.Library import Library
from klasy.Employee import Employee
from klasy.Book import Book
from klasy.Student_2 import Student
from klasy.Order import Order

library1 = Library("Rybnik", "Rudzka", "44-200",
                   "Pon-Pt 8-16", "32 0156111")
library2 = Library("Katowice", "Zielona", "55-300",
                   "Pon-Pt 8-16", "32 1238760")


employee1 = Employee("Adam", "Nowak", "20-05-2015", "30-01-1985",
                     "Poznań", "Wielkopolski", "33-220", "+48 072 309 111")
employee2 = Employee("Paweł", "Woźniak", "02-06-2022", "30-01-1990",
                     "Wisła", "Zielona", "12-111", "+48 492 765 999")
employee3 = Employee("Marcin", "Wiśniewski", "20-05-2011", "30-01-1979",
                     "Częstochowa", "Powstańców", "87-555", "+48 333 876 333")


book1 = Book(library1, "14-03-1970", "Adam", "Nowacki", "500")
book2 = Book(library2, "24-09-2000", "Ewa", "Wiśniewska", "87")
book3 = Book(library1, "03-11-1999", "Jan", "Woźniak", "145")
book4 = Book(library2, "23-02-1989", "Dawid", "Kos", "229")
book5 = Book(library1, "09-06-1977", "Michał", "Kowalczyk", "111")


student1 = Student('Max', 'Czarniecki')
student2 = Student('Joanna', 'Matelska')
student3 = Student('Marian', 'Wincent')


Order1 = Order(employee1, student1, book1, "20-07-2023")
Order2 = Order(employee2, student2, book2, "04-09-2024")

print(Order1)
print(Order2)
