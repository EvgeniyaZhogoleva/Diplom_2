import requests
import allure
from data import DataURL
from data import DataAnswerText
from conftest import TestAuthUserChange

base_url = f'{DataURL.BASE_URL}/api/auth/user'


class TestChangeUserData:
    @allure.title('Изменение данных авторизованного пользователя')
    def test_change_user_data(self):
        auth_user = TestAuthUserChange()
        token = auth_user.auth_token_change()
        headers = {
            "Authorization": f"Bearer {token}"
        }
        payload = {
            "email": "89762У@ya.ru",
            "password": "6543210",
            "name": "jane"
        }
        response = requests.patch(base_url, json=payload, headers=headers, timeout=10)
        assert 403 == response.status_code

    @allure.title('Изменение данных неавторизованного пользователя')
    def test_change_user_data_without_auth(self):
        payload = {
            "email": "6811823@ya.ru",
            "password": "1234567",
            "name": "jane"
        }
        response = requests.patch(base_url, json=payload)
        assert 401 == response.status_code
        assert response.json()["message"] == DataAnswerText.REQUEST_WITHOUT_AUTH["message"]





