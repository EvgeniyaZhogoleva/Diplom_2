import requests
import allure
from data import DataURL
from data import DataAnswerText
from data import Ingredients
from conftest import auth_user


base_url = f'{DataURL.BASE_URL}/api/orders'

class TestNewOrder:

    @allure.title('Создание заказа с авторизацией')
    @allure.description('Создание нового заказа с авторизацией и ингредиентами')
    def test_new_order_with_auth_user_and_ingredients(self, auth_user):
        ingredients_data = Ingredients.INGREDIENTS
        headers = {"Authorization": auth_user}
        response = requests.post(base_url, json=ingredients_data, headers=headers, timeout=10)
        assert response.status_code == 200


    @allure.description('Создание нового заказа с авторизацией и без ингредиентов')
    def test_new_order_with_auth_user_and_without_ingredients(self, auth_user):
        ingredients_data = Ingredients.EMPTY_INGREDIENTS
        headers = {"Authorization": auth_user}
        response = requests.post(base_url, json=ingredients_data, headers=headers, timeout=10)
        assert response.status_code == 400
        assert response.json()["message"] == DataAnswerText.WITHOUT_INGREDIENTS["message"]


    @allure.description('Создание нового заказа с авторизацией с неправильным хэшем ингредиента')
    def test_new_order_with_auth_user_and_wrong_hash_ingredients(self, auth_user):
        ingredients_data = Ingredients.WRONG_INGREDIENTS
        headers = {"Authorization": auth_user}
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
        ingredients_data = Ingredients.EMPTY_INGREDIENTS
        response = requests.post(base_url, json=ingredients_data, timeout=10)
        assert response.status_code == 400
        assert response.json()["message"] == DataAnswerText.WITHOUT_INGREDIENTS["message"]



















