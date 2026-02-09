import requests
from url import URL

class CreateOrderMethods:
    @staticmethod
    def create_order(body):
        return requests.post(url=URL.CREATE_ORDER, json=body)