import random
import string
import requests
from data import DataURL


base_url = f'{DataURL.BASE_URL}/api/auth/user'

class TestUser:
    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def __init__(self):
        self.email = self.generate_random_string(6) + '@yandex.ru'
        self.password = self.generate_random_string(6)
        self.name = self.generate_random_string(6)
        self.NEW_USER = {
            "email": self.email,
            "password": self.password,
            "name": self.name
        }

class TestAuthUser:
    def auth_token(self):
        url = 'https://stellarburgers.nomoreparties.site/api/auth/login'
        payload = {
            "email": "zho1goleva_6811823@ya.ru",
            "password": "123456",
            "name": "Женя"
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            json_response = response.json()
            access_token = json_response.get('accessToken')
            return access_token
        else:
            raise Exception(f"Failed to get access token: {response.status_code} - {response.text}")


class TestAuthUserChange:
    def auth_token_change(self):
        url = 'https://stellarburgers.nomoreparties.site/api/auth/login'
        payload = {
            "email": "123456rr@yandex.ru",
            "password": "654321",
            "name": "Alice"
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            json_response = response.json()
            access_token = json_response.get('accessToken')
            return access_token
        else:
            raise Exception(f"Failed to get access token: {response.status_code} - {response.text}")
