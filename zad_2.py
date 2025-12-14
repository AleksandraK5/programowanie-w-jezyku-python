class Library:
    def __init__(self, city: str, street: str, zip_code: str,
                 open_hours: str, phone: str) -> None:
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (f'Library in {self.street} {self.city} {self.zip_code}'
                f' Open Hours: {self.open_hours} Phone: {self.phone}')


library1 = Library("Rybnik", "Rudzka", "44-200",
                   "Pon-Pt 8-16", "32 0156111")
library2 = Library("Katowice", "Zielona", "55-300",
                   "Pon-Pt 8-16", "32 1238760")


class Employee:
    def __init__(self, first_name: str, last_name: str,
                 hire_date: str, birth_date: str,
                 city: str, street: str, zip_code: str, phone: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f'Employee: {self.first_name} {self.last_name}, '
                f'Adress: {self.street} {self.city} {self.zip_code} '
                f'Phone: {self.phone} '
                f'Hire date: {self.hire_date} '
                f'Birth date: {self.birth_date}'
                )


employee1 = Employee("Adam", "Nowak", "20-05-2015", "30-01-1985",
                     "Poznań", "Wielkopolski", "33-220", "+48 072 309 111")
employee2 = Employee("Paweł", "Woźniak", "02-06-2022", "30-01-1990",
                     "Wisła", "Zielona", "12-111", "+48 492 765 999")
employee3 = Employee("Marcin", "Wiśniewski", "20-05-2011", "30-01-1979",
                     "Częstochowa", "Powstańców", "87-555", "+48 333 876 333")


class Book:
    def __init__(self, library: Library, publication_date: str,
                 author_name: str, author_surname: str,
                 number_of_pages: str) -> None:
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f'Book by: {self.author_name} {self.author_surname} '
                f'Pages: {self.number_of_pages} '
                f'Published: {self.publication_date}\n'
                f'{self.library}')


book1 = Book(library1, "14-03-1970", "Adam", "Nowacki", "500")
book2 = Book(library2, "24-09-2000", "Ewa", "Wiśniewska", "87")
book3 = Book(library1, "03-11-1999", "Jan", "Woźniak", "145")
book4 = Book(library2, "23-02-1989", "Dawid", "Kos", "229")
book5 = Book(library1, "09-06-1977", "Michał", "Kowalczyk", "111")


class Student:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'


student1 = Student('Max', 'Czarniecki')
student2 = Student('Joanna', 'Matelska')
student3 = Student('Marian', 'Wincent')


class Order:
    def __init__(self, employee: Employee, student: Student,
                 books: Book, order_date: str) -> None:
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return (f'{self.employee}\n{self.student}\n'
                f'{self.books}\nOrder date: {self.order_date}\n')


Order1 = Order(employee1, student1, book1, "20-07-2023")
Order2 = Order(employee2, student2, book2, "04-09-2024")

print(Order1)
print(Order2)
