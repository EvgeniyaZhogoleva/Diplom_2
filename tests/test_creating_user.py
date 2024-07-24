import requests
import allure
from data import DataURL
from data import DataAnswerText
from conftest import TestUser

base_url = f'{DataURL.BASE_URL}/api/auth/register'

class TestCreateNewUser:

    @allure.title('Тест создания нового пользователя')
    @allure.description('Тест создания уникального пользователя')
    def test_create_new_user(self):
        test_courier = TestUser()
        payload = test_courier.NEW_USER
        response = requests.post(base_url, json=payload)
        assert 200 == response.status_code


    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_create_existing_user(self):
        payload = {
            "email": "test-data@yandex.ru",
            "password": "123456",
            "name": "Username"
        }
        response = requests.post(base_url, json=payload)
        assert 403 == response.status_code
        assert response.json()["message"] == DataAnswerText.USER_ALREADY_EXIST["message"]


    @allure.title('Создание пользователя без заполнения обязательного поля')
    def test_create_user_missing_field(self):
        payload = {
            "email": "test-data@yandex.ru",
        }
        response = requests.post(base_url, json=payload)
        assert 403 == response.status_code
        assert response.json()["message"] == DataAnswerText.NOT_ENOUGH_DATA_FOR_CREATE["message"]






