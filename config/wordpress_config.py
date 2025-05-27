import os

from dotenv import load_dotenv


class WordPressBDConfig:
    """Класс, описывающий параметры соединения с БД WordPress"""
    load_dotenv()
    HOST = os.environ.get("HOST")
    PORT = int(os.environ.get("PORT"))
    USER = os.environ.get("USER")
    PASSWORD = os.environ.get("PASSWORD")

    DB = "wordpress"
    AUTOCOMMIT = True

    TABLE_WP_POSTS = "wp_posts"
    TABLE_WP_TERMS = "wp_terms"
    TABLE_WP_TERM_TAXONOMY = "wp_term_taxonomy"
    TABLE_WP_USERS = "wp_users"


class WordPressURLS:
    """Класс, описывающий набор url-адресов, необходимых для API тестов"""
    # url-адрес хоста сервиса
    HOST_URL = "http://localhost:8000/index.php?rest_route="

    # url-адреса для управления записями
    POSTS_GET_URL = f"{HOST_URL}/wp/v2/posts/" # при использовании необходимо добавлять id
    POSTS_GET_ALL_URL = f"{HOST_URL}/wp/v2/posts"
    POSTS_CREATE_URL = f"{HOST_URL}/wp/v2/posts"
    POSTS_UPDATE_URL = f"{HOST_URL}/wp/v2/posts/" # при использовании необходимо добавлять id
    POSTS_DELETE_URL = f"{HOST_URL}/wp/v2/posts/" # при использовании необходимо добавлять id

    # url-адреса для управления рубриками
    CATEGORIES_GET_URL = f"{HOST_URL}/wp/v2/categories/" # при использовании необходимо добавлять id
    CATEGORIES_GET_ALL_URL = f"{HOST_URL}/wp/v2/categories"
    CATEGORIES_CREATE_URL = f"{HOST_URL}/wp/v2/categories"
    CATEGORIES_UPDATE_URL = f"{HOST_URL}/wp/v2/categories/" # при использовании необходимо добавлять id
    CATEGORIES_DELETE_URL = f"{HOST_URL}/wp/v2/categories/" # при использовании необходимо добавлять id

    # url-адреса для управления метками
    TAGS_GET_URL = f"{HOST_URL}/wp/v2/tags/" # при использовании необходимо добавлять id
    TAGS_GET_ALL_URL = f"{HOST_URL}/wp/v2/tags"
    TAGS_CREATE_URL = f"{HOST_URL}/wp/v2/tags"
    TAGS_UPDATE_URL = f"{HOST_URL}/wp/v2/tags/" # при использовании необходимо добавлять id
    TAGS_DELETE_URL = f"{HOST_URL}/wp/v2/tags/" # при использовании необходимо добавлять id

    # url-адреса для управления пользователями
    USERS_GET_URL = f"{HOST_URL}/wp/v2/users/" # при использовании необходимо добавлять id
    USERS_GET_ALL_URL = f"{HOST_URL}/wp/v2/users"
    USERS_CREATE_URL = f"{HOST_URL}/wp/v2/users"
    USERS_UPDATE_URL = f"{HOST_URL}/wp/v2/users/" # при использовании необходимо добавлять id
    USERS_DELETE_URL = f"{HOST_URL}/wp/v2/users/" # при использовании необходимо добавлять id