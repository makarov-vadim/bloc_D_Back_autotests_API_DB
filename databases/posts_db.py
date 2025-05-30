import logging
from typing import Any

import allure

from config.wordpress_config import WordPressBDConfig
from databases.wordpress_db import WordPressDB
from helpers.api_helpers import get_post_from_db
from helpers.sql_queries import SQLQueries
from models.models import PostModel


class PostsDB(WordPressDB):
    """Класс, описывающий создание, получение и удаление записей в базе данных WordPressDB"""
    @allure.step("Создание записи в БД с помощью SQL-запроса")
    def create_post(self, post: PostModel) -> int:
        logging.info(f"Создание записи {post} в БД с помощью SQL-запроса")

        sql_query = SQLQueries.create_post_query(post.title, post.content, post.status)
        return self._execute(sql_query)


    @allure.step("Получение записи из БД с помощью SQL-запроса")
    def get_post(self, post_id: int) -> PostModel | None:
        logging.info(f"Получение записи с id {post_id} из БД с помощью SQL-запроса")

        sql_query = SQLQueries.get_post_query(post_id)
        response = self._get_object(sql_query)
        post_from_db = get_post_from_db(response)

        logging.info(f"Результат SQL-запроса на получение записи: {post_from_db}")
        return post_from_db


    @allure.step("Удаление записи из БД с помощью SQL-запроса")
    def delete_post(self, post_id) -> Any:
        logging.info(f"Удаление записи с id {post_id} из БД с помощью SQL-запроса")
        return self._delete_object(WordPressBDConfig.TABLE_WP_POSTS, post_id)
