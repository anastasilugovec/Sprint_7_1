import pytest
import allure
import data
from methods.create_order_methods import CreateOrderMethods

class TestCreateOrder:
    @allure.title('Создание заказа.')
    @allure.description('Проверяет, что можно создать заказ с разными вариантами цвета')
    @pytest.mark.parametrize('color', (['BLACK'], ['GREY'], ['BLACK', 'GREY'], None))
    def test_create_order(self, color):
        order_info = data.order_data(color)
        response = CreateOrderMethods.create_order(order_info)

        assert response.status_code == 201
        assert "track" in response.json()