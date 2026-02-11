import requests
from url import URL

class OrderListMethods:
    @staticmethod
    def get_orders():
        return requests.get(url=URL.ORDER_LIST)