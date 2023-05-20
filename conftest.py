import pytest



@pytest.fixture()
def get_base_url():
    return "https://reqres.in/api/"