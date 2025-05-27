import allure

from config.wordpress_config import WordPressBDConfig
from databases.wordpress_db import WordPressDB
from helpers.sql_queries import SQLQueries
from models.models import PostModel


class PostsDB(WordPressDB):
    """Класс, описывающий создание, получение и удаление записей в базе данных WordPressDB"""
    @allure.step("Создание записи в БД с помощью SQL-запроса")
    def create_post(self, post: PostModel):
        """Создание записи в БД с помощью SQL-запроса"""
        sql_query = SQLQueries.create_post_query(post.title, post.content, post.status)
        return self._execute(sql_query)

    @allure.step("Получение записи из БД с помощью SQL-запроса")
    def get_post(self, post_id: int) -> dict | None:
        """Получение записи из БД с помощью SQL-запроса"""
        sql_query = SQLQueries.get_post_query(post_id)
        return self._get_object(sql_query)

    @allure.step("Удаление записи из БД с помощью SQL-запроса")
    def delete_post(self, post_id):
        """Удаление записи из БД с помощью SQL-запроса"""
        return self._delete_object(WordPressBDConfig.TABLE_WP_POSTS, post_id)
