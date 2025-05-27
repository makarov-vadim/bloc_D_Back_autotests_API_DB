import allure
from requests import Response

from api.wordpress_api import WordPressApi
from config.wordpress_config import WordPressURLS
from models.models import UserModel


class UsersApi(WordPressApi):
    """Класс, описывающий создание, обновление и удаление пользователя на сервисе через API"""
    @allure.step("Создание пользователя")
    def create_user(self, user: UserModel) -> Response:
        """Создание пользователя"""
        return self.create_object(WordPressURLS.USERS_CREATE_URL, user.model_dump())

    @allure.step("Обновление пользователя")
    def update_user(self, user_id: int, data: dict) -> Response:
        """Обновление пользователя"""
        return self.update_object(WordPressURLS.USERS_UPDATE_URL, user_id, data)

    @allure.step("Удаление пользователя")
    def delete_user(self, user_id: int, delete_data: dict) -> Response:
        """Удаление пользователя"""
        return self.delete_object(WordPressURLS.USERS_DELETE_URL, user_id, delete_data)
