import functools
from typing import Any

import pymysql


class BaseDB:
    """Класс, описывающий базовый набор действий с базой данных"""
    def __init__(self, connection_info: dict):
        self.connection_info = connection_info

        self._select_all = self._sql_request(self._select_all)
        self._execute = self._sql_request(self._execute)

    def _sql_request(self, func):
        """Декоратор для работы с курсором библиотеки pymysql"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with pymysql.connect(**self.connection_info) as connect:
                with connect.cursor() as cursor:
                    result = func(*args, cursor=cursor, **kwargs)
            return result
        return wrapper

    def _select_all(self, sql, args=None, cursor=None) -> tuple:
        """Метод, выполняющий SELECT-запрос в БД"""
        cursor.execute(sql,args)
        columns = [desc[0] for desc in cursor.description]
        result = cursor.fetchall()
        return columns, result

    def _execute(self, sql, args=None, cursor=None) -> Any:
        """Метод, выполняющий запрос в БД"""
        cursor.execute(sql, args)
        return cursor.lastrowid
