import requests
from url import URL

class LoginCourierMethods:
    @staticmethod
    def login_courier(body):
      return requests.post(url=URL.CREATE_COURIER, json=body)
