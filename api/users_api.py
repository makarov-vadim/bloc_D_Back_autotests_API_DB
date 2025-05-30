import logging

import allure

from api.wordpress_api import WordPressApi
from config.wordpress_config import WordPressURLS
from helpers.api_helpers import get_user_from_api
from models.models import UserModel


class UsersApi(WordPressApi):
    """Класс, описывающий создание, обновление и удаление пользователя на сервисе через API"""
    @allure.step("Создание пользователя")
    def create_user(self, user: UserModel) -> UserModel:
        logging.info(f"Создание пользователя {user}")
        response_body = self.create_object(WordPressURLS.USERS_CREATE_URL, user.model_dump())
        return get_user_from_api(response_body)

    @allure.step("Обновление пользователя")
    def update_user(self, user_id: int, data: dict) -> UserModel | None:
        logging.info(f"Обновление пользователя с id {user_id} и обновляемыми параметрами {data}")
        response_body = self.update_object(WordPressURLS.USERS_UPDATE_URL, user_id, data)
        return get_user_from_api(response_body)

    @allure.step("Удаление пользователя")
    def delete_user(self, user_id: int, delete_data: dict) -> UserModel | None:
        logging.info(f"Удаление пользователя c id {user_id}")
        response_body = self.delete_object(WordPressURLS.USERS_DELETE_URL, user_id, delete_data)
        return get_user_from_api(response_body)
