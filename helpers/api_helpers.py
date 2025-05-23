from helpers.models import PostModel, CategoryModel, TagModel, UserModel


def get_post(post_data: dict) -> PostModel:
    """Функция, генерирующая модель записи"""
    return PostModel(**post_data)

def get_category(category_data: dict) -> CategoryModel:
    """Функция, генерирующая модель рубрики"""
    return CategoryModel(**category_data)

def get_tag(tag_data: dict) -> TagModel:
    """Функция, генерирующая модель метки"""
    return TagModel(**tag_data)

def get_user(user_data: dict) -> UserModel:
    """Функция, генерирующая модель пользователя"""
    return UserModel(**user_data)


def get_post_from_db(sql_response: dict | None) -> PostModel | None:
    """Функция, возвращающая модель записи, считанную из БД"""
    if sql_response is None:
        return None
    post_data = {
        "id": sql_response["ID"],
        "title": sql_response["post_title"],
        "content": sql_response["post_content"],
        "status": sql_response["post_status"]
    }
    return get_post(post_data)

def get_post_from_api(api_response: dict) -> PostModel:
    """Функция, возвращающая модель записи, считанную из ответа на REST-запрос"""
    post_data = {
        "id": api_response["id"],
        "title": api_response["title"]["raw"],
        "content": api_response["content"]["raw"],
        "status": api_response["status"]
    }
    return get_post(post_data)


def get_category_from_db(sql_response: dict | None) -> CategoryModel | None:
    """Функция, возвращающая модель рубрики, считанную из БД"""
    if sql_response is None:
        return None
    category_data = {
        "id": sql_response["term_taxonomy_id"],
        "name": sql_response["name"],
        "taxonomy": sql_response["taxonomy"]
    }
    return get_category(category_data)


def get_category_from_api(api_response: dict) -> CategoryModel:
    """Функция, возвращающая модель рубрики, считанную из ответа на REST-запрос"""
    category_data = {
        "id": api_response["id"],
        "name": api_response["name"],
        "taxonomy": api_response["taxonomy"],
    }
    return get_category(category_data)


def get_tag_from_bd(sql_response: dict | None) -> TagModel | None:
    """Функция, возвращающая модель метки, считанную из БД"""
    if sql_response is None:
        return None
    tag_data = {
        "id": sql_response["term_taxonomy_id"],
        "name": sql_response["name"],
        "taxonomy": sql_response["taxonomy"]
    }
    return get_tag(tag_data)

def get_tag_from_api(api_response: dict) -> TagModel:
    """Функция, возвращающая модель метки, считанную из ответа на REST-запрос"""
    tag_data = {
        "id": api_response["id"],
        "name": api_response["name"],
        "taxonomy": api_response["taxonomy"],
    }
    return get_tag(tag_data)

def get_user_from_bd(sql_response: dict | None) -> UserModel | None:
    """Функция, возвращающая модель пользователя, считанную из БД"""
    if sql_response is None:
        return None
    user_data = {
        "id": sql_response["ID"],
        "username": sql_response["user_login"],
        "email": sql_response["user_email"],
    }
    return get_user(user_data)

def get_user_from_api(api_response: dict) -> UserModel:
    """Функция, возвращающая модель метки, считанную из ответа на REST-запрос"""
    user_data = {
        "id": api_response["id"],
        "username": api_response["username"],
        "email": api_response["email"]
    }
    return get_user(user_data)
