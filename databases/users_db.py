import allure

from config.wordpress_config import WordPressBDConfig
from databases.wordpress_db import WordPressDB
from helpers.sql_queries import SQLQueries
from models.models import UserModel


class UsersDB(WordPressDB):
    """Класс, описывающий создание, получение и удаление пользователей в базе данных WordPressDB"""
    @allure.step("Создание пользователя в БД с помощью SQL-запроса")
    def create_user(self, user: UserModel):
        """Создание пользователя в БД с помощью SQL-запроса"""
        sql_query = SQLQueries.create_user_query(user.username, user.email, user.password)
        return self._execute(sql_query)

    @allure.step("Получение пользователя из БД с помощью SQL-запроса")
    def get_user(self, user_id):
        """Получение пользователя из БД с помощью SQL-запроса"""
        sql_query = SQLQueries.get_user_query(user_id)
        return self._get_object(sql_query)

    @allure.step("Удаление пользователя из БД с помощью SQL-запроса")
    def delete_user(self, user_id):
        """Удаление пользователя из БД с помощью SQL-запроса"""
        return self._delete_object(WordPressBDConfig.TABLE_WP_USERS, user_id)
