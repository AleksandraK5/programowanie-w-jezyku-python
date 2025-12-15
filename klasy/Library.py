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
