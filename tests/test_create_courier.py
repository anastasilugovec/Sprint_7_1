import pytest
import allure


class TestCreateCourier:
    @allure.title('Создание курьера')
    @allure.description('Проверка, что курьера можно создать и возвращается код 201 и {"ok": true}.')
    def test_create_courier(self):
        body = DataForCourier.get_create_courier_body()
        response = CreateCourierMethods.create_courier(body)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title('Создание двух одинаковых курьеров')
    @allure.description('Проверка создания двух курьеров с одинаковыми данными. Ожидается ошибка при дублировании.')
    def test_create_duplicate_courier(self):
        body = DataForCourier.get_create_courier_body()

        response_first = CreateCourierMethods.create_courier(body)
        assert response_first.status_code == 201
        assert response_first.json() == {"ok": True}

        response_second = CreateCourierMethods.create_courier(body)
        assert response_second.status_code == 409
        assert response_second.json()['message'] == data.CREATE_COURIER_DUPLICATION_ERROR

    @allure.description('Проверка, что нельзя создать курьера с пустым обязательным полем (логин или пароль).')
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_with_missing_field(self, missing_field):
        courier_data = generate_new_courier_personal_data(empty_field=missing_field)
        response = CreateCourierMethods.create_courier(courier_data)
        assert response.status_code == 400
        assert response.json()["message"] == data.CREATE_COURIER_EMPTY_FIELD_ERROR

    @allure.title('Создание курьера с логином, который уже есть')
    @allure.description('Проверка, что нельзя создать курьера с логином, который уже есть.')
    def test_create_courier_existing_login(self):
        courier_data = generate_new_courier_personal_data()
        response = CreateCourierMethods.create_courier(courier_data)
        assert response.status_code == 201

        new_data = generate_new_courier_personal_data()
        new_data['login'] = courier_data['login']
        create_response = CreateCourierMethods.create_courier(new_data)

        assert create_response.status_code == 409
        assert create_response.json()["message"] == data.CREATE_COURIER_DUPLICATION_ERROR