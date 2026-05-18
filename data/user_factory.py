from config import USER_EMAIL, USER_PASSWORD
from data.user import User


class UserFactory:

    @staticmethod
    def correct_existing_user():
        return User(email=USER_EMAIL, password=USER_PASSWORD)

    @staticmethod
    def correct_nonexisting_user():
        return User(email="user@mail.com", password="12345678")

    @staticmethod
    def user_with_incorrect_email():
        return User(email="user", password="12345678")

    @staticmethod
    def user_with_incorrect_password():
        return User(email="user@mail.com", password="1234567")
