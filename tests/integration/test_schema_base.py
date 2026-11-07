import pytest
from pydantic import ValidationError
from app.schemas.base import UserBase, PasswordMixin, UserCreate, UserLogin

def test_user_base_valid():
    data = {
        "first_name": "King",
        "last_name": "Diamond",
        "email": "King.Diamond@example.com",
        "username": "kingdiamond",
    }
    user = UserBase(**data)
    assert user.first_name == "King"
    assert user.last_name == "Diamond"
    assert user.email == "King.Diamond@example.com"
    assert user.username == "kingdiamond"

def test_user_base_invalid_email():
    data = {
        "first_name": "King",
        "last_name": "Diamond",
        "email": "invalid-email",
        "username": "kingdiamond",
    }
    with pytest.raises(ValidationError):
        UserBase(**data)


def test_password_mixin_valid():
    data = {"password": "SecurePass123"}
    password_mixin = PasswordMixin(**data)
    assert password_mixin.password == "SecurePass123"


def test_password_mixin_invalid_short_password():
    data = {"password": "short"}
    with pytest.raises(ValidationError, match="Password must be at least 6 characters long, fool!"):
        PasswordMixin(**data)


def test_password_no_uppercase():
    data = {"password": "lowercase1"}
    with pytest.raises(ValidationError, match="Password must contain at least one uppercase letter, fool!"):
        PasswordMixin(**data)


def test_password_mixin_no_lowercase():
    data = {"password": "UPPERCASE1"}
    with pytest.raises(ValidationError, match="Password must contain at least one lowercase letter, fool!"):
        PasswordMixin(**data)


def test_password_mixin_no_digit():
    data = {"password": "NoDigitsHere"}
    with pytest.raises(ValidationError, match="Password must contain at least one digit, fool!"):
        PasswordMixin(**data)


def test_user_create_valid():
    data = {
        "first_name": "King",
        "last_name": "Diamond",
        "email": "King.Diamond@example.com",
        "username": "kingdiamond",
        "password": "SecurePass123",
    }
    user_create = UserCreate(**data)
    assert user_create.username == "kingdiamond"
    assert user_create.password == "SecurePass123"


def test_user_create_invalid_password():
    data = {
        "first_name": "King",
        "last_name": "Diamond",
        "email": "King.Diamond@example.com",
        "username": "kingdiamond",
        "password": "short",
    }
    with pytest.raises(ValidationError):
        UserCreate(**data)


def test_user_login_valid():
    data = {"username": "kingdiamond", "password": "SecurePass123"}
    user_login = UserLogin(**data)
    assert user_login.username == "kingdiamond"


def test_user_login_invalid_username():
    data = {"username": "kd", "password": "SecurePass123"}
    with pytest.raises(ValidationError):
        UserLogin(**data)


def test_user_login_invalid_password():
    data = {"username": "kingdiamond", "password": "short"}
    with pytest.raises(ValidationError):
        UserLogin(**data)

