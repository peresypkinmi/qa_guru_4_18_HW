import random
from datetime import datetime

from Objects.User import User
from pytest_voluptuous import S
from Models.UserModel import *


class Step:
    """dict for keeping expected results of parameters which get executing steps of test"""
    EXPECTED_DICT = {}

    """dict for keeping actual results of parameters which get executing steps of test"""
    ACTUAL_DICT = {}

    def get_user_quantity(self):
        """step gets user quantity and saves it in EXPECTED_DICT and ACTUAL_DICT"""

        data_users = User.get_user_list(1)
        self.EXPECTED_DICT['total'] = data_users['total']
        self.ACTUAL_DICT['total'] = 0
        for i in range(1, data_users['total_pages'] + 1):
            self.ACTUAL_DICT['total'] += len(User.get_user_list(i)['data'])

    def get_token_after_register(self):
        user = User()
        self.ACTUAL_DICT['token'] = user.register_user()['token']

    def get_status_code_user_list_response(self):
        self.EXPECTED_DICT['status_code'] = 200
        self.ACTUAL_DICT['status_code'] = User.get_status_code_user_list()

    def get_status_code_unsuccessful_register(self):
        user = User()
        self.ACTUAL_DICT['status_code'] = user.register_user_without_pass().status_code
        self.EXPECTED_DICT['status_code'] = 400

    def get_total_page_parameter(self):
        self.ACTUAL_DICT['total_pages'] = User.get_user_list()['total_pages']
        self.ACTUAL_DICT['total'] = User.get_user_list()['total']
        self.ACTUAL_DICT['per_page'] = User.get_user_list()['per_page']

    def create_new_user(self):
        self.EXPECTED_DICT['name'] = 'test'
        self.EXPECTED_DICT['job'] = 'test'
        user = User().create_user(name='test', job='test')
        self.ACTUAL_DICT['name'] = user.name
        self.ACTUAL_DICT['job'] = user.job

    def get_data_creating_user(self):
        user = User().create_user('test', 'test')
        self.ACTUAL_DICT['createdAt'] = user.createdAt[2:10]

    def register_user_without_password(self):
        user = User()
        self.ACTUAL_DICT['error_message'] = user.register_user_without_pass().json()['error']
        self.EXPECTED_DICT['error_message'] = 'Missing password'

    def get_users_list(self):
        page = 1
        self.ACTUAL_DICT['response'] = []
        while True:
            response = User.get_user_list(page=page)
            self.ACTUAL_DICT['response'].append(response)
            if response['total_pages'] > page:
                page += 1
            else:
                break

    def get_random_single_user_from_user_list(self):
        response_item = random.randint(0, len(self.ACTUAL_DICT['response']) - 1)
        data_user_item = random.randint(0, len(self.ACTUAL_DICT['response'][response_item]['data']) - 1)
        self.ACTUAL_DICT['single_user'] = self.ACTUAL_DICT['response'][response_item]['data'][data_user_item]
        self.EXPECTED_DICT['single_user'] = User.get_single_user(self.ACTUAL_DICT['single_user']['id'])

    def assert_single_user_to_user_from_list(self):
        assert self.EXPECTED_DICT['single_user']['data'] == self.ACTUAL_DICT['single_user']

    def assert_lenght_token(self):
        assert len(self.ACTUAL_DICT['token']) == 17

    def assert_users_list_model(self):
        for i in range(len(self.ACTUAL_DICT['response'])):
            assert S(UserModels.list_users_model) == self.ACTUAL_DICT['response'][i]

    def assert_error_message(self):
        assert self.ACTUAL_DICT['error_message'] == self.EXPECTED_DICT['error_message']

    def assert_existing_user(self):
        assert self.ACTUAL_DICT['name'] == self.EXPECTED_DICT['name']
        assert self.ACTUAL_DICT['job'] == self.EXPECTED_DICT['job']

    def assert_date_creating_user(self):
        self.EXPECTED_DICT['createdAt'] = datetime.today().strftime('%y-%m-%d')
        assert self.ACTUAL_DICT['createdAt'] == self.EXPECTED_DICT['createdAt']

    def assert_total_pages(self):
        assert self.ACTUAL_DICT['total_pages'] == self.ACTUAL_DICT['total'] // self.ACTUAL_DICT['per_page']

    def assert_quantity_users(self):
        """assertion total quantity from ACTUAL_DICT and EXPECTED_DICT"""

        assert self.ACTUAL_DICT['total'] == self.EXPECTED_DICT['total']

    def assert_status_code(self):
        assert self.ACTUAL_DICT['status_code'] == self.EXPECTED_DICT['status_code']
