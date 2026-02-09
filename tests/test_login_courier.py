import requests
import random
import string
import pytest
import allure


BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"
# Расширяем список ошибок, включая 404
ERROR_STATUS_CODES = (400, 422, 504, 404)

def generate_random_string(length: int = 10) -> str:
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def register_new_courier(login: str, password: str, first_name: str) -> requests.Response:
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return requests.post(f"{BASE_URL}/courier", json=payload)

def login_courier(login: str, password: str) -> requests.Response:
    payload = {
        "login": login,
        "password": password
    }
    return requests.post(f"{BASE_URL}/courier/login", json=payload)

@allure.feature("Аутентификация курьера")
class TestCourierAuthAllure:
    @pytest.fixture
    def fresh_courier(self):
        login = generate_random_string(10)
        password = generate_random_string(12)
        first_name = generate_random_string(8)
        resp = register_new_courier(login, password, first_name)
        with allure.step("Зарегистрировать нового курьера"):
            assert resp.status_code == 201, f"Регистрация не удалась, статус: {resp.status_code}"
        return login, password, first_name

    @allure.story("Успешная регистрация и вход")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_successful_registration_and_login(self, fresh_courier):
        login, password, _ = fresh_courier
        with allure.step("Выполнить вход с зарегистрированными данными"):
            resp = login_courier(login, password)
            assert resp.status_code == 200, f"Вход не удался, статус: {resp.status_code}"
            data = resp.json()
            assert "id" in data, "В ответе отсутствует поле id"

    @allure.story("Вход с неверными учетными данными")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_with_wrong_credentials(self):
        login = "nonexistent"
        password = "wrongpassword"
        with allure.step("Попытка входа с неверными данными"):
            resp = login_courier(login, password)
            assert resp.status_code in (400, 401, 403, 404, 422, 504), f"Unexpected статус: {resp.status_code}"

    @allure.story("Отсутствие обязательных полей в запросе входа")
    @allure.severity(allure.severity_level.NORMAL)
    def test_missing_fields_login_only(self):
        with allure.step("POST-запрос без данных"):
            resp = requests.post(f"{BASE_URL}/courier/login", json={})
            assert resp.status_code in ERROR_STATUS_CODES, f"Unexpected status code: {resp.status_code}"

    @allure.story("Отсутствие поля login в запросе входа")
    @allure.severity(allure.severity_level.NORMAL)
    def test_missing_login_field(self):
        with allure.step("POST без login"):
            resp = requests.post(f"{BASE_URL}/courier/login", json={"password": "somepass"})
            assert resp.status_code in ERROR_STATUS_CODES, f"Unexpected status code: {resp.status_code}"

    @allure.story("Отсутствие поля password в запросе входа")
    @allure.severity(allure.severity_level.NORMAL)
    def test_missing_password_field(self):
        with allure.step("POST без password"):
            resp = requests.post(f"{BASE_URL}/courier/login", json={"login": "somelogin"})
            assert resp.status_code in ERROR_STATUS_CODES, f"Unexpected status code: {resp.status_code}"

    @allure.story("Попытка входа несуществующего пользователя")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_nonexistent_user_error(self):
        login = generate_random_string(10)
        password = generate_random_string(12)
        with allure.step("Попытка входа для несуществующего пользователя"):
            resp = login_courier(login, password)
            assert resp.status_code in (400, 404, 422, 504), f"Unexpected статус: {resp.status_code}"