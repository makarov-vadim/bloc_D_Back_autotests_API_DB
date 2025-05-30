from config.wordpress_config import WordPressBDConfig
from databases.base_db import BaseDB
from helpers.sql_queries import SQLQueries


class WordPressDB(BaseDB):
    """Класс, описывающий общий набор действий с базой данных WordPressDB"""
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

    def _delete_object(self, table_name, obj_id, obj_id_name="id"):
        """Метод, выполняющий запрос на удаление объекта"""
        sql_query = SQLQueries.delete_query(table_name, obj_id, obj_id_name)
        return self._execute(sql_query)

    def _get_object(self, sql_query: str) -> dict | None:
        """Метод, выполняющий запрос на получение объекта"""
        columns, results = self._select_all(sql_query)
        if not results:
            return None
        return dict(zip(columns, results[0]))

    def _get_term_taxonomy(self, term_taxonomy_id: int, taxonomy: str):
        """Метод, выполняющий запрос на получение объекта из таблицы wp_term_taxonomy"""
        sql_query = SQLQueries.get_taxonomy_query(term_taxonomy_id, taxonomy)
        return self._get_object(sql_query)

    def _delete_term_taxonomy(self, term_taxonomy_id: int, taxonomy: str):
        """Метод, выполняющий запрос на удаление объекта из таблицы wp_term_taxonomy"""
        category_data = self._get_term_taxonomy(term_taxonomy_id, taxonomy)
        if category_data is None:
            return None
        term_id = category_data["term_id"]

        self._delete_object(WordPressBDConfig.TABLE_WP_TERM_TAXONOMY, term_taxonomy_id, obj_id_name="term_taxonomy_id")
        self._delete_object(WordPressBDConfig.TABLE_WP_TERMS, term_id, obj_id_name="term_id")
