import logging
from typing import Any

import allure

from config.wordpress_config import WordPressBDConfig
from databases.wordpress_db import WordPressDB
from helpers.api_helpers import get_user_from_bd
from helpers.sql_queries import SQLQueries
from models.models import UserModel


class UsersDB(WordPressDB):
    """Класс, описывающий создание, получение и удаление пользователей в базе данных WordPressDB"""
    @allure.step("Создание пользователя в БД с помощью SQL-запроса")
    def create_user(self, user: UserModel) -> int:
        logging.info(f"Создание пользователя {user} в БД с помощью SQL-запроса")

        sql_query = SQLQueries.create_user_query(user.username, user.email, user.password)
        return self._execute(sql_query)


    @allure.step("Получение пользователя из БД с помощью SQL-запроса")
    def get_user(self, user_id) -> UserModel | None:
        logging.info(f"Получение пользователя с id {user_id} из БД с помощью SQL-запроса")

        sql_query = SQLQueries.get_user_query(user_id)
        response = self._get_object(sql_query)
        user_from_db = get_user_from_bd(response)

        logging.info(f"Результат SQL-запроса на получение пользователя: {user_from_db}")
        return user_from_db


    @allure.step("Удаление пользователя из БД с помощью SQL-запроса")
    def delete_user(self, user_id) -> Any:
        logging.info(f"Удаление пользователя с id {user_id} из БД с помощью SQL-запроса")
        return self._delete_object(WordPressBDConfig.TABLE_WP_USERS, user_id)
