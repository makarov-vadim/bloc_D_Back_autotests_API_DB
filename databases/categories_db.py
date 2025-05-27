import allure

from databases.wordpress_db import WordPressDB
from helpers.sql_queries import SQLQueries
from models.models import CategoryModel


class CategoriesDB(WordPressDB):
    """Класс, описывающий создание, получение и удаление рубрик в базе данных WordPressDB"""
    @allure.step("Создание рубрики в БД с помощью SQL-запроса")
    def create_category(self, category: CategoryModel):
        """Создание рубрики в БД с помощью SQL-запроса"""
        sql_query_1 = SQLQueries.create_term_query(category.name)
        response_1 = self._execute(sql_query_1)
        sql_query_2 = SQLQueries.create_taxonomy_query(response_1, "category")
        response_2 = self._execute(sql_query_2)
        return response_2

    @allure.step("Получение рубрики из БД с помощью SQL-запроса")
    def get_category(self, term_taxonomy_id: int):
        """Получение рубрики из БД с помощью SQL-запроса"""
        return self._get_term_taxonomy(term_taxonomy_id, "category")

    @allure.step("Удаление рубрики из БД с помощью SQL-запроса")
    def delete_category(self, term_taxonomy_id: int):
        """Удаление рубрики из БД с помощью SQL-запроса"""
        return self._delete_term_taxonomy(term_taxonomy_id, "category")





