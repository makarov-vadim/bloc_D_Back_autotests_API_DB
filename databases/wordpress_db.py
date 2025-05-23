import allure
from databases.base_db import BaseDB
from config.wordpress_config import WordPressBDConfig
from helpers.models import PostModel, CategoryModel, TagModel, UserModel
from helpers.sql_queries import SQLQueries

class WordPressDB(BaseDB):
    def __init__(self):
        connection_info = {
            "host": WordPressBDConfig.HOST,
            "port": WordPressBDConfig.PORT,
            "user": WordPressBDConfig.USER,
            "password": WordPressBDConfig.PASSWORD,
            "db": WordPressBDConfig.DB,
            "autocommit": WordPressBDConfig.AUTOCOMMIT
        }
        super().__init__(connection_info)

    # Общие методы
    def _delete_object(self, table_name, obj_id, obj_id_name="id"):
        sql_query = SQLQueries.delete_query(table_name, obj_id, obj_id_name)
        return self._execute(sql_query)

    def _get_object(self, sql_query: str) -> dict | None:
        columns, results = self._select_all(sql_query)
        if not results:
            return None
        return dict(zip(columns, results[0]))

    def _get_term_taxonomy(self, term_taxonomy_id: int, taxonomy: str):
        sql_query = SQLQueries.get_taxonomy_query(term_taxonomy_id, taxonomy)
        return self._get_object(sql_query)

    def _delete_term_taxonomy(self, term_taxonomy_id: int, taxonomy: str):
        category_data = self._get_term_taxonomy(term_taxonomy_id, taxonomy)
        if category_data is None:
            return None
        term_id = category_data["term_id"]

        self._delete_object(WordPressBDConfig.TABLE_WP_TERM_TAXONOMY, term_taxonomy_id, obj_id_name="term_taxonomy_id")
        self._delete_object(WordPressBDConfig.TABLE_WP_TERMS, term_id, obj_id_name="term_id")
        return


    # Создание, получение и удаление записи
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


    # Создание, получение и удаление рубрики
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


    # Создание, получение и удаление метки
    @allure.step("Создание метки в БД с помощью SQL-запроса")
    def create_tag(self, tag: TagModel):
        """Создание метки в БД с помощью SQL-запроса"""
        sql_query_1 = SQLQueries.create_term_query(tag.name)
        response_1 = self._execute(sql_query_1)
        sql_query_2 = SQLQueries.create_taxonomy_query(response_1, "post_tag")
        response_2 = self._execute(sql_query_2)
        return response_2

    @allure.step("Получение метки из БД с помощью SQL-запроса")
    def get_tag(self, term_taxonomy_id: int):
        """Получение метки из БД с помощью SQL-запроса"""
        return self._get_term_taxonomy(term_taxonomy_id, "post_tag")

    @allure.step("Удаление метки из БД с помощью SQL-запроса")
    def delete_tag(self, term_taxonomy_id: int):
        """Удаление метки из БД с помощью SQL-запроса"""
        return self._delete_term_taxonomy(term_taxonomy_id, "post_tag")


    # Создание, получение и удаление пользователя
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


    # Отчистка БД перед тестом и после теста
    @allure.step("Отчистка БД перед тестом и после теста")
    def delete_all_data(self):
        """Отчистка БД перед тестом и после теста"""
        sql_queries = [
            SQLQueries.delete_all_query(WordPressBDConfig.TABLE_WP_POSTS),
            SQLQueries.delete_all_query(WordPressBDConfig.TABLE_WP_TERMS),
            SQLQueries.delete_all_query(WordPressBDConfig.TABLE_WP_TERM_TAXONOMY),
            SQLQueries.delete_users_query()
        ]
        results = [self._execute(sql_query) for sql_query in sql_queries]
        return results
