import requests
import allure
from data import DataURL
from data import DataAnswerText
from conftest import TestAuthUser

base_url = f'{DataURL.BASE_URL}/api/orders'

class TestGetOrder:

    @allure.title('Получение заказа конкретного пользователя с авторизацией')
    def test_get_order_for_authorized_user(self):
        auth_user = TestAuthUser()
        token = auth_user.auth_token()
        headers={"Authorization": token}
        response = requests.get(base_url, headers=headers, timeout=10)
        assert response.status_code == 200


    @allure.title('Получение заказа конкретного пользователя без авторизации')
    def test_get_order_without_auth(self):
        response = requests.get(base_url)
        assert response.status_code == 401
        assert response.json()["message"] == DataAnswerText.REQUEST_WITHOUT_AUTH["message"]





