import allure
from methods.order_list_methods import OrderListMethods


class TestOrderList:
    @allure.title('Получение списка заказов.')
    @allure.description('Проверяет, что в тело ответа возвращается список заказов.')
    def test_list_orders(self):
        response = OrderListMethods.get_orders()

        assert response.status_code == 200
        assert "orders" in response.json()