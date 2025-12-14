class Property:
    def __init__(self, area: int, rooms: int,
                 price: int, address: str) -> None:
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area: int, rooms: int,
                 price: int, address: str, plot: int) -> None:
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (f'House at {self.address}\n'
                f'Area: {self.area}m2, Rooms: {self.rooms}, '
                f'Plot: {self.plot}m2, Price: {self.price}PLN\n')


class Flat(Property):
    def __init__(self, area: int, rooms: int,
                 price: int, address: str, floor: int) -> None:
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (f'Flat at {self.address}\n'
                f'Area: {self.area}m2, Rooms: {self.rooms}, '
                f'Floor: {self.floor}, Price: {self.price}PLN\n')


house = House(180, 7, 700000, "49 Małopolska, Kraków", 700)
flat = Flat(50, 2, 100000, "23b Przyjaźń, Bytom", 5)

print(house)
print(flat)
