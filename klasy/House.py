from klasy.Property import Property


class House(Property):
    def __init__(self, area: int, rooms: int,
                 price: int, address: str, plot: int) -> None:
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (f'House at {self.address}\n'
                f'Area: {self.area}m2, Rooms: {self.rooms}, '
                f'Plot: {self.plot}m2, Price: {self.price}PLN\n')
