import allure
from requests import Response

from api.base_api import BaseApi
from config.auth_config import AuthConfig
from config.wordpress_config import WordPressURLS

from typing import Any


from helpers.models import PostModel, CategoryModel, TagModel, UserModel


class WordPressApi(BaseApi):
    """Класс, описывающий тестовый сервис, который предоставляет
    точки доступа для управления сущностями через API"""
    def __init__(self):
        self.auth_info = (AuthConfig.USERNAME, AuthConfig.PASSWORD)
        self.urls = {
            "posts": {
                "get": WordPressURLS.POSTS_GET_URL,
                "get_all": WordPressURLS.POSTS_GET_ALL_URL,
                "create": WordPressURLS.POSTS_CREATE_URL,
                "update": WordPressURLS.POSTS_UPDATE_URL,
                "delete": WordPressURLS.POSTS_DELETE_URL
            },
            "categories": {
                "get": WordPressURLS.CATEGORIES_GET_URL,
                "get_all": WordPressURLS.CATEGORIES_GET_ALL_URL,
                "create": WordPressURLS.CATEGORIES_CREATE_URL,
                "update": WordPressURLS.CATEGORIES_UPDATE_URL,
                "delete": WordPressURLS.CATEGORIES_DELETE_URL
            },
            "tags": {
                "get": WordPressURLS.TAGS_GET_URL,
                "get_all": WordPressURLS.TAGS_GET_ALL_URL,
                "create": WordPressURLS.TAGS_CREATE_URL,
                "update": WordPressURLS.TAGS_UPDATE_URL,
                "delete": WordPressURLS.TAGS_DELETE_URL
            },
            "users": {
                "get": WordPressURLS.USERS_GET_URL,
                "get_all": WordPressURLS.USERS_GET_ALL_URL,
                "create": WordPressURLS.USERS_CREATE_URL,
                "update": WordPressURLS.USERS_UPDATE_URL,
                "delete": WordPressURLS.USERS_DELETE_URL
            }
        }


    def create_object(self, endpoint_name: str, data: Any) -> Response:
        """Метод, создающий сущность на сервисе"""
        return self._request_post(auth=self.auth_info, url=self.urls[endpoint_name]["create"], json=data)

    def get_object(self, endpoint_name: str, object_id) -> Response:
        """Метод, получающий сущность из сервиса"""
        return self._request_get(auth=self.auth_info, url=f"{self.urls[endpoint_name]["get"]}{object_id}")

    def get_all_objects(self, endpoint_name: str) -> Response:
        """Метод, получающий все сущности из сервиса"""
        return self._request_get(auth=self.auth_info, url=self.urls[endpoint_name]["get_all"])

    def update_object(self, endpoint_name: str, object_id, data) -> Response:
        """Метод, обновляющий сущность на сервисе"""
        return self._request_post(auth=self.auth_info, url=f"{self.urls[endpoint_name]["update"]}{object_id}", json=data)

    def delete_object(self, endpoint_name: str, object_id, data) -> Response:
        """Метод, удаляющий сущность на сервисе"""
        return self._request_delete(auth=self.auth_info, url=f"{self.urls[endpoint_name]["delete"]}{object_id}", json=data)


    # Создание, обновление и удаление записи на сервисе
    @allure.step("Создание записи на сервисе с помощью POST-запроса")
    def create_post(self, post: PostModel) -> Response:
        """Создание записи на сервисе с помощью POST-запроса"""
        return self.create_object("posts", post.model_dump())

    @allure.step("Обновление записи на сервисе с помощью POST-запроса")
    def update_post(self, post_id, data) -> Response:
        """Обновление записи на сервисе с помощью POST-запроса"""
        return self.update_object("posts", post_id, data)

    @allure.step("Удаление записи на сервисе с помощью DELETE-запроса")
    def delete_post(self, post_id, delete_data):
        """Удаление записи на сервисе с помощью DELETE-запроса"""
        return  self.delete_object("posts", post_id, delete_data)


    # Создание, обновление и удаление рубрики на сервисе
    @allure.step("Создание рубрики на сервисе с помощью POST-запроса")
    def create_category(self, category: CategoryModel) -> Response:
        """Создание рубрики на сервисе с помощью POST-запроса"""
        return self.create_object("categories", category.model_dump())

    @allure.step("Обновление рубрики на сервисе с помощью POST-запроса")
    def update_category(self, category_id, data) -> Response:
        """Обновление рубрики на сервисе с помощью POST-запроса"""
        return self.update_object("categories", category_id, data)

    @allure.step("Удаление рубрики на сервисе с помощью DELETE-запроса")
    def delete_category(self, category_id, delete_data):
        """Удаление рубрики на сервисе с помощью DELETE-запроса"""
        return  self.delete_object("categories", category_id, delete_data)


    # Создание, обновление и удаление метки на сервисе
    @allure.step("Создание метки на сервисе с помощью POST-запроса")
    def create_tag(self, tag: TagModel) -> Response:
        """Создание метки на сервисе с помощью POST-запроса"""
        return self.create_object("tags", tag.model_dump())

    @allure.step("Обновление метки на сервисе с помощью POST-запроса")
    def update_tag(self, tag_id, data) -> Response:
        """Обновление метки на сервисе с помощью POST-запроса"""
        return self.update_object("tags", tag_id, data)

    @allure.step("Удаление метки на сервисе с помощью DELETE-запроса")
    def delete_tag(self, tag_id, delete_data):
        """Удаление метки на сервисе с помощью DELETE-запроса"""
        return  self.delete_object("tags", tag_id, delete_data)


    # Создание, обновление и удаление пользователя на сервисе
    @allure.step("Создание пользователя на сервисе с помощью POST-запроса")
    def create_user(self, user: UserModel) -> Response:
        """Создание пользователя на сервисе с помощью POST-запроса"""
        return self.create_object("users", user.model_dump())

    @allure.step("Обновление пользователя на сервисе с помощью POST-запроса")
    def update_user(self, user_id, data) -> Response:
        """Обновление пользователя на сервисе с помощью POST-запроса"""
        return self.update_object("users", user_id, data)

    @allure.step("Удаление пользователя на сервисе с помощью DELETE-запроса")
    def delete_user(self, user_id, delete_data):
        """Удаление пользователя на сервисе с помощью DELETE-запроса"""
        return  self.delete_object("users", user_id, delete_data)