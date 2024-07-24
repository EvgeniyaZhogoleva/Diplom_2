import requests
import allure
from data import DataURL
from data import DataAnswerText
from data import Ingredients
from conftest import TestAuthUser


base_url = f'{DataURL.BASE_URL}/api/orders'

class TestNewOrder:

    @allure.title('Создание заказа с авторизацией')
    @allure.description('Создание нового заказа с авторизацией и ингредиентами')
    def test_new_order_with_auth_user_and_ingredients(self):
        auth_user = TestAuthUser()
        token = auth_user.auth_token()
        ingredients_data = Ingredients.INGREDIENTS
        headers = {"Authorization": token}
        response = requests.post(base_url, json=ingredients_data, headers=headers, timeout=10)
        assert response.status_code == 200


    @allure.description('Создание нового заказа с авторизацией и без ингредиентов')
    def test_new_order_with_auth_user_and_without_ingredients(self):
        auth_user = TestAuthUser()
        token = auth_user.auth_token()
        ingredients_data = {
            "ingredients": []
        }
        headers = {"Authorization": token}
        response = requests.post(base_url, json=ingredients_data, headers=headers, timeout=10)
        assert response.status_code == 400
        assert response.json()["message"] == DataAnswerText.WITHOUT_INGREDIENTS["message"]


    @allure.description('Создание нового заказа с авторизацией с неправильным хэшем ингредиента')
    def test_new_order_with_auth_user_and_wrong_hash_ingredients(self):
        auth_user = TestAuthUser()
        token = auth_user.auth_token()
        ingredients_data = {
            "ingredients": ["11223344"]
        }
        headers = {"Authorization": token}
        response = requests.post(base_url, json=ingredients_data, headers=headers, timeout=10)
        assert response.status_code == 500


    @allure.title('Создание заказа без авторизации')
    @allure.description('Создание нового заказа без авторизации но с ингредиентами')
    def test_new_order_without_auth_user_and_ingredients(self):
        ingredients_data = Ingredients.INGREDIENTS
        response = requests.post(base_url, json=ingredients_data, timeout=10)
        assert response.status_code == 200


    @allure.description('Создание нового заказа без авторизации и без ингредиентов')
    def test_new_order_without_auth_user_and_without_ingredients(self):
        ingredients_data = {
            "ingredients": []
        }
        response = requests.post(base_url, json=ingredients_data, timeout=10)
        assert response.status_code == 400
        assert response.json()["message"] == DataAnswerText.WITHOUT_INGREDIENTS["message"]



















