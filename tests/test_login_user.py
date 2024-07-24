import requests
import allure
from data import DataURL
from data import DataAnswerText
from data import TestData


base_url = f'{DataURL.BASE_URL}/api/auth/login'

class TestUserLogin:

    @allure.title('Логин пользователя')
    @allure.description('Логин под существующим пользователем')
    def test_successful_login(self):
        payload = TestData.AUTH_PAYLOAD
        response = requests.post(base_url, json=payload)
        assert 200 == response.status_code


    @allure.description('Логин с неверным логином и паролем')
    def test_login_with_invalid_login_and_password(self):
        payload = {
            "email": "invalid@ya.ru",
            "password": "987654"
        }
        response = requests.post(base_url, json=payload)
        assert 401 == response.status_code
        assert response.json()["message"] == DataAnswerText.INVALID_LOGIN_PASSWORD["message"]



