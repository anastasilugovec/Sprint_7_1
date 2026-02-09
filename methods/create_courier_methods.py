import requests
from url import URL

class CreateCourierMethods:

    @staticmethod
    def create_courier(body):
        return requests.post(url=URL.CREATE_COURIER, json=body)
    @staticmethod
    def login_courier(login_body):
        return requests.post(url=URL.LOGIN_COURIER, json=login_body)

