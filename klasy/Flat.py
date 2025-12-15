from klasy.Property import Property


class Flat(Property):
    def __init__(self, area: int, rooms: int,
                 price: int, address: str, floor: int) -> None:
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (f'Flat at {self.address}\n'
                f'Area: {self.area}m2, Rooms: {self.rooms}, '
                f'Floor: {self.floor}, Price: {self.price}PLN\n')
