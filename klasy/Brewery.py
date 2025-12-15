class Brewery:
    def __init__(self, id: str, name: str,
                 address_1: str, address_2: str, address_3: str,
                 city: str, state_province: str, postal_code: str,
                 country: str, longitude: int, latitude: int,
                 phone: str, website_url: str, state: str, street: str,
                 brewery_type=['micro', 'regional', 'brewpub', 'planning',
                               'large', 'bar', 'contract',
                               'nano', 'proprietor', 'closed']):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.address_1 = address_1
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state_province = state_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.state = state
        self.street = street

    def __str__(self):
        return (f'Brewery ID: {self.id}, Brewery Name: {self.name}, '
                f'Brewery type: {self.brewery_type}\n'
                f'Street: {self.street} City: {self.city} '
                f'State: {self.state} Province: {self.state_province} \n'
                f'Address: {self.address_1}, {self.address_2}, '
                f'{self.address_3}, '
                f'Code: {self.postal_code} Country: {self.country}\n'
                f'Geographic Coordinates: {self.longitude}, {self.latitude}\n'
                f'Phone: {self.phone} Website: {self.website_url}\n')
