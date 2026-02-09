import random
import string

def generate_random_string(length=10):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))

CREATE_COURIER_DUPLICATION_ERROR = "Этот логин уже используется. Попробуйте другой."
CREATE_COURIER_EMPTY_FIELD_ERROR = "Недостаточно данных для создания учетной записи"
LOGIN_WITH_INCORRECT_CREDENTIALS_ERROR = "Учетная запись не найдена"
LOGIN_WITH_EMPTY_FIELD_ERROR = "Недостаточно данных для входа"


def order_data(color=''):
    data = {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "Москва, ул. Ленина, д. 1",
        "metroStation": "Краснопресненская",
        "phone": "+79991112233",
        "rentTime": 5,
        "deliveryDate": "2023-12-31",
        "comment": "Тестовый заказ",
        "totalPrice": 1000,
    }
    if color:
        data["color"] = color
    return data

def generate_new_courier_personal_data(empty_field=None):
    data = {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string()
    }
    if empty_field:
        data[empty_field] = ''
    return data

class DataForCourier:
    @staticmethod
    def get_create_courier_body():
        return {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

courier_data = {
    "login": "test_login",
    "password": "test_password",
    "firstName": "Test"
}