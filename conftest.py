import pytest
from helpers import generate_random_string
import requests

BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"

def register_new_courier(login: str, password: str, first_name: str):
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return requests.post(f"{BASE_URL}/courier", json=payload)

def login_courier(login: str, password: str):
    payload = {
        "login": login,
        "password": password
    }
    return requests.post(f"{BASE_URL}/courier/login", json=payload)

def delete_courier(courier_id: int):
    return requests.delete(f"{BASE_URL}/courier/{courier_id}")

@pytest.fixture
def fresh_courier():
    login = generate_random_string(10)
    password = generate_random_string(12)
    first_name = generate_random_string(8)
    resp = register_new_courier(login, password, first_name)
    return login, password, first_name, resp


def delete_courier():
    return None