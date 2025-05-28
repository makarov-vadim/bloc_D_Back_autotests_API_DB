import logging

import allure

from databases.wordpress_db import WordPressDB
from helpers.api_helpers import get_tag_from_bd
from helpers.sql_queries import SQLQueries
from models.models import TagModel


class TagsDB(WordPressDB):
    """Класс, описывающий создание, получение и удаление меток в базе данных WordPressDB"""
    @allure.step("Создание метки в БД с помощью SQL-запроса")
    def create_tag(self, tag: TagModel) -> int:
        """Создание метки в БД с помощью SQL-запроса"""
        logging.info(f"Создание метки {tag} в БД с помощью SQL-запроса")

        sql_query_1 = SQLQueries.create_term_query(tag.name)
        response_1 = self._execute(sql_query_1)
        sql_query_2 = SQLQueries.create_taxonomy_query(response_1, "post_tag")
        response_2 = self._execute(sql_query_2)
        return response_2


    @allure.step("Получение метки из БД с помощью SQL-запроса")
    def get_tag(self, term_taxonomy_id: int) -> TagModel | None:
        """Получение метки из БД с помощью SQL-запроса"""
        logging.info(f"Получение метки с id {term_taxonomy_id} из БД с помощью SQL-запроса")

        response = self._get_term_taxonomy(term_taxonomy_id, "post_tag")
        tag_from_db = get_tag_from_bd(response)

        logging.info(f"Результат SQL-запроса на получение метки: {tag_from_db}")
        return tag_from_db


    @allure.step("Удаление метки из БД с помощью SQL-запроса")
    def delete_tag(self, term_taxonomy_id: int) -> None:
        """Удаление метки из БД с помощью SQL-запроса"""
        logging.info(f"Удаление метки с id {term_taxonomy_id} из БД с помощью SQL-запроса")
        return self._delete_term_taxonomy(term_taxonomy_id, "post_tag")
