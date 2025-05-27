import allure
from requests import Response

from api.wordpress_api import WordPressApi
from config.wordpress_config import WordPressURLS
from models.models import PostModel


class PostsApi(WordPressApi):
    """Класс, описывающий создание, обновление и удаление записи на сервисе через API"""
    @allure.step("Создание записи")
    def create_post(self, post: PostModel) -> Response:
        """Создание записи"""
        return self.create_object(WordPressURLS.POSTS_CREATE_URL, post.model_dump())

    @allure.step("Обновление записи")
    def update_post(self, post_id: int, data: dict) -> Response:
        """Обновление записи"""
        return self.update_object(WordPressURLS.POSTS_UPDATE_URL, post_id, data)

    @allure.step("Удаление записи")
    def delete_post(self, post_id: int, delete_data: dict) -> Response:
        """Удаление записи"""
        return self.delete_object(WordPressURLS.POSTS_DELETE_URL, post_id, delete_data)
