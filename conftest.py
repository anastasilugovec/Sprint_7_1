import requests
import pytest
from helpers import generate_random_string
BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"

def register_new_courier(login: str, password: str, first_name: str) -> requests.Response:
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return requests.post(f"{BASE_URL}/courier", json=payload)


@pytest.fixture
def fresh_courier():
    login = generate_random_string(10)
    password = generate_random_string(12)
    first_name = generate_random_string(8)
    resp = register_new_courier(login, password, first_name)
    return login, password, first_name, resp