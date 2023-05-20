import requests


class Request:
    BASE_URL = "https://reqres.in/api/"
    BODY = {}

    @staticmethod
    def get(entity, id: str = '', page=1):
        return requests.get(f'{Request.BASE_URL}{entity}/{id}?page={page}')

    @staticmethod
    def post(entity):
        return requests.post(f'{Request.BASE_URL}{entity}', json=Request.BODY)
