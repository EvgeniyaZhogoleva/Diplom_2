class DataURL:

    BASE_URL = 'https://stellarburgers.nomoreparties.site'

class DataAnswerText:

    USER_ALREADY_EXIST = {"message": "User already exists"}
    NOT_ENOUGH_DATA_FOR_CREATE = {"message": "Email, password and name are required fields"}
    INVALID_LOGIN_PASSWORD = {"message": "email or password are incorrect"}
    REQUEST_WITHOUT_AUTH = {"message": "You should be authorised"}
    WITHOUT_INGREDIENTS = {"message": "Ingredient ids must be provided"}



class TestData:
    AUTH_PAYLOAD = payload = {
            "email": "zho1goleva_6811823@ya.ru",
            "password": "123456"
        }

class Ingredients:
    INGREDIENTS = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
        }

