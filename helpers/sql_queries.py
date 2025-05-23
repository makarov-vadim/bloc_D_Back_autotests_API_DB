class SQLQueries:
    """Класс, описывающий набор SQL-запросов для работы с БД WordPress"""

    @staticmethod
    def get_columns_query(table_name):
        sql_query = f"SELECT GROUP_CONCAT(`COLUMN_NAME`) FROM `INFORMATION_SCHEMA`.`COLUMNS`WHERE `TABLE_SCHEMA` = 'wordpress' AND `TABLE_NAME` = '{table_name}';"
        return sql_query

    @staticmethod
    def delete_query(table_name, obj_id, obj_id_name="id"):
        sql_query = f"DELETE FROM {table_name} WHERE {obj_id_name}={obj_id};"
        return sql_query

    @staticmethod
    def delete_all_query(table_name):
        sql_query = f"DELETE FROM {table_name};"
        return sql_query

    @staticmethod
    def delete_users_query():
        sql_query = f"DELETE FROM wp_users WHERE id <> 1;"
        return sql_query

    @staticmethod
    def create_post_query(post_title, post_content, post_status):
        sql_query = ("INSERT INTO wp_posts ("
                        "post_author, "
                        "post_date, "
                        "post_date_gmt, "
                        "post_content, "
                        "post_title, "
                        "post_excerpt,"
                        "post_status, "
                        "to_ping, "
                        "pinged, "
                        "post_modified, "
                        "post_modified_gmt, "
                        "post_content_filtered"
                     ") "
                     "VALUES ("
                        "1, "
                        "DATE_ADD(NOW(), INTERVAL 3 HOUR), "
                        "NOW(), "
                        f"'{post_content}', "
                        f"'{post_title}', "
                        f"'', "
                        f"'{post_status}', "
                        f"'', "
                        f"'', "
                        "DATE_ADD(NOW(), INTERVAL 3 HOUR), "
                        "NOW(), "
                        "''"
                     ");"
                     )
        return sql_query

    @staticmethod
    def get_post_query(post_id):
        sql_query = ("SELECT "
                     "ID, "
                     "post_title, "
                     "post_content, "
                     "post_status "
                     f"FROM wp_posts WHERE id={post_id};")
        return sql_query


    @staticmethod
    def create_term_query(term_name):
        sql_query = ("INSERT INTO wp_terms ("
                        "name"
                     ") "
                     "VALUES ("
                        f"'{term_name}'"
                     ");"
                     )
        return sql_query

    @staticmethod
    def create_taxonomy_query(term_id, taxonomy):
        sql_query = ("INSERT INTO wp_term_taxonomy ("
                        "term_id, "
                        "taxonomy, "
                        "description"
                     ") "
                     "VALUES ("
                        f"{term_id}, "
                        f"'{taxonomy}', "
                        "''"
                     ");"
                     )
        return sql_query

    @staticmethod
    def get_term_query(term_id):
        sql_query = f"SELECT * FROM wp_terms WHERE term_id={term_id};"
        return sql_query

    @staticmethod
    def get_taxonomy_query(term_taxonomy_id, taxonomy):
        sql_query = (f"SELECT "
                        "term_taxonomy_id, "
                        "term_id, "
                        "taxonomy, "
                        "name "
                     "FROM "
                        "wp_term_taxonomy "
                     "JOIN wp_terms USING(term_id) "
                     f"WHERE term_taxonomy_id={term_taxonomy_id} AND taxonomy='{taxonomy}';")
        return sql_query

    @staticmethod
    def create_user_query(username, email, password):
        sql_query = ("INSERT INTO wp_users ("
                        "user_login, "
                        "user_pass, "
                        "user_email, "
                        "user_registered"
                     ") "
                     "VALUES ("
                        f"'{username}', "
                        f"'{hash(password)}', "
                        f"'{email}', "
                        "NOW()"
                     ");"
                     )
        return sql_query

    @staticmethod
    def get_user_query(user_id):
        sql_query = ("SELECT "
                     "ID, "
                     "user_login, "
                     "user_email, "
                     "user_pass "
                     f"FROM wp_users WHERE id={user_id};")
        return sql_query

