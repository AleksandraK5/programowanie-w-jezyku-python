from typing import List
import requests
from klasy.Brewery import Brewery
URL_API = 'https://api.openbrewerydb.org/v1/breweries'


def get_breweries_from_api() -> List[Brewery]:
    par = {'per_page': 20}
    response = requests.get(URL_API, params=par)
    data = response.json()
    breweries = []
    for bdata in data:
        brewery = Brewery(
            id=bdata.get('id'),
            name=bdata.get('name'),
            brewery_type=bdata.get('brewery_type'),
            address_1=bdata.get('address_1'),
            address_2=bdata.get('address_2'),
            address_3=bdata.get('address_3'),
            city=bdata.get('city'),
            state_province=bdata.get('state_province'),
            postal_code=bdata.get('postal_code'),
            country=bdata.get('country'),
            longitude=bdata.get('longitude'),
            latitude=bdata.get('latitude'),
            phone=bdata.get('phone'),
            website_url=bdata.get('website_url'),
            state=bdata.get('state'),
            street=bdata.get('street')
        )
        breweries.append(brewery)
    return breweries


def main():
    breweries = get_breweries_from_api()
    for brewery in breweries:
        print(brewery)


if __name__ == "__main__":
    main()
