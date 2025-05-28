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
        """Создание пользователя"""
        logging.info(f"Создание пользователя {user}")

        response = self.create_object(WordPressURLS.USERS_CREATE_URL, user.model_dump())
        assert response.status_code == 201, "Статус-код ответа неверный"
        user_from_api = get_user_from_api(response.json())

        logging.info(f"Статус-код ответа на запрос создания пользователя: {response.status_code}")
        logging.info(f"Результат запроса создания пользователя: {user_from_api}")
        return user_from_api


    @allure.step("Обновление пользователя")
    def update_user(self, user_id: int, data: dict) -> UserModel | None:
        """Обновление пользователя"""
        logging.info(f"Обновление пользователя с id {user_id} и обновляемыми параметрами {data}")

        response = self.update_object(WordPressURLS.USERS_UPDATE_URL, user_id, data)
        assert response.status_code == 200, "Статус-код ответа неверный"
        user_from_api = get_user_from_api(response.json())

        logging.info(f"Статус-код ответа на запрос обновления пользователя: {response.status_code}")
        logging.info(f"Результат запроса обновления пользователя: {user_from_api}")
        return user_from_api


    @allure.step("Удаление пользователя")
    def delete_user(self, user_id: int, delete_data: dict) -> UserModel | None:
        """Удаление пользователя"""
        logging.info(f"Удаление пользователя c id {user_id}")

        response = self.delete_object(WordPressURLS.USERS_DELETE_URL, user_id, delete_data)
        assert response.status_code == 200, "Статус-код ответа неверный"
        user_from_api = get_user_from_api(response.json())

        logging.info(f"Статус-код ответа на запрос удаления пользователя: {response.status_code}")
        logging.info(f"Результат запроса удаления пользователя: {user_from_api}")
        return user_from_api
