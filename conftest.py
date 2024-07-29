import pytest
from helpers import TestAuthUser, TestAuthUserChange


@pytest.fixture
def auth_user():
    auth = TestAuthUser()
    token = auth.auth_token()
    return token

@pytest.fixture
def auth_user_change():
    auth = TestAuthUserChange()
    token = auth.auth_token_change()
    return token