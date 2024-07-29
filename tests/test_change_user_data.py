import requests
import allure
from data import DataURL, DataAnswerText, TestData
from conftest import auth_user_change

base_url = f'{DataURL.BASE_URL}/api/auth/user'


class TestChangeUserData:
    @allure.title('Изменение данных авторизованного пользователя')
    def test_change_user_data(self, auth_user_change):
        headers = {"Authorization": auth_user_change}
        payload = TestData.CHANGE_DATA
        response = requests.patch(base_url, json=payload, headers=headers, timeout=10)
        assert 403 == response.status_code

    @allure.title('Изменение данных неавторизованного пользователя')
    def test_change_user_data_without_auth(self):
        payload = TestData.CHANGE_DATA
        response = requests.patch(base_url, json=payload)
        assert 401 == response.status_code
        assert response.json()["message"] == DataAnswerText.REQUEST_WITHOUT_AUTH["message"]





