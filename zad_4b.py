from typing import List
import requests
import argparse
from klasy.Brewery import Brewery
URL_API = 'https://api.openbrewerydb.org/v1/breweries'


def get_breweries_from_api(city: str | None) -> List[Brewery]:
    if city is not None:
        response = requests.get(f'{URL_API}?by_city={city}')
        data = response.json()
        return data
    else:
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


def get_args():
    parser = argparse.ArgumentParser(description='Fetch breweries')
    parser.add_argument('-c', '--city',
                        help='Filter brewery by city', required=False)
    return vars(parser.parse_args())


def main():
    args = get_args()
    breweries1 = get_breweries_from_api(city=args['city'])
    print(f'{breweries1}\n')
    print(f'{len(breweries1)}\n')

    breweries2 = get_breweries_from_api(None)
    for brewery in breweries2:
        print(brewery)


if __name__ == "__main__":
    main()
