from dataclasses import dataclass
from request.Request import *


@dataclass()
class User:
    id: int = 0
    name: str = ''
    job: str = ''
    createdAt: str = ''

    def create_user(self, job: str, name: str):
        Request.BODY = {'job': job,
                        'name': name}
        data_user = Request.post('users').json()
        return User(data_user['id'], data_user['name'], data_user['job'], data_user['createdAt'])

    def register_user(self):
        Request.BODY = {"email": "eve.holt@reqres.in",
                        "password": "pistol"}
        data_user = Request.post('register').json()
        return data_user

    def register_user_without_pass(self):
        Request.BODY = {"email": "eve.holt@reqres.in"}
        data_user = Request.post('register')
        return data_user

    @staticmethod
    def get_user_list(page: int = 1):
        return Request.get('users', page=page).json()

    @staticmethod
    def get_single_user(id: int):
        return Request.get('users', id=id).json()

    @staticmethod
    def get_status_code_user_list():
        return Request.get('users', page=1).status_code
