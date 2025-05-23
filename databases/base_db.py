import pymysql
from typing import Any

class BaseDB:
    def __init__(self, connection_info: dict):
        self.connection_info = connection_info

    def _select(self, sql, args=None) -> tuple | None:
        with pymysql.connect(**self.connection_info) as conn:
            with conn.cursor() as cur:
                cur.execute(sql,args)
                columns = [desc[0] for desc in cur.description]
                result = cur.fetchone()
        return columns, result

    def _select_all(self, sql, args=None) -> tuple:
        with pymysql.connect(**self.connection_info) as conn:
            with conn.cursor() as cur:
                cur.execute(sql,args)
                columns = [desc[0] for desc in cur.description]
                result = cur.fetchall()
        return columns, result

    def _execute(self, sql, args=None) -> Any:
        with pymysql.connect(**self.connection_info) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, args)
                return cur.lastrowid

    def _execute_many(self, sql, args=None) -> Any:
        with pymysql.connect(**self.connection_info) as conn:
            with conn.cursor() as cur:
                return cur.executemany(sql, args)

