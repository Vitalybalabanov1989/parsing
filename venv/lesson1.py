from copy import copy
import requests
import json


class Product:
    name = 'NOT NAME'

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return self.name


class CatalogParser:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }

    def __init__(self, start_url: str):
        self.__start_url: str = start_url
        self.__product_list: list = []

    def parse(self):
        url: str = self.__start_url
        while url:
            response = requests.get(url, headers=self.headers)
            data = response.json()
            url = data.get('next')
            test = [Product(**itm) for itm in data.get('results')]
            self.__product_list.extend([Product(**itm) for itm in data.get('results')])

    @property
    def products(self):
        return copy(self.__product_list)


if __name__ == '__main__':
    parser = CatalogParser('https://5ka.ru/api/v2/special_offers/')
    parser.parse()
    print(1)

#
# any_object = {
#     'one': [1, 2, 3, 4],
#     'two': (9, 2, 3, 4, 5),
#     'tree': True,
#     'four': None,
#     'five': 'ANY "STR"ING',
#
# }

# j_data = json.dumps(any_object)
# print(j_data)
