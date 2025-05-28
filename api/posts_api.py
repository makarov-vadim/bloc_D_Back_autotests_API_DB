import logging

import allure

from api.wordpress_api import WordPressApi
from config.wordpress_config import WordPressURLS
from helpers.api_helpers import get_post_from_api
from models.models import PostModel


class PostsApi(WordPressApi):
    """Класс, описывающий создание, обновление и удаление записи на сервисе через API"""
    @allure.step("Создание записи")
    def create_post(self, post: PostModel) -> PostModel:
        """Создание записи"""
        logging.info(f"Создание записи {post}")

        response = self.create_object(WordPressURLS.POSTS_CREATE_URL, post.model_dump())
        assert response.status_code == 201, "Статус-код ответа неверный"
        post_from_api = get_post_from_api(response.json())

        logging.info(f"Статус-код ответа на запрос создания записи: {response.status_code}")
        logging.info(f"Результат запроса создания записи: {post_from_api}")
        return post_from_api


    @allure.step("Обновление записи")
    def update_post(self, post_id: int, data: dict) -> PostModel | None:
        """Обновление записи"""
        logging.info(f"Обновление записи с id {post_id} и обновляемыми параметрами {data}")

        response = self.update_object(WordPressURLS.POSTS_UPDATE_URL, post_id, data)
        assert response.status_code == 200, "Статус-код ответа неверный"
        post_from_api = get_post_from_api(response.json())

        logging.info(f"Статус-код ответа на запрос обновления записи: {response.status_code}")
        logging.info(f"Результат запроса обновления записи: {post_from_api}")
        return post_from_api


    @allure.step("Удаление записи")
    def delete_post(self, post_id: int, delete_data: dict) -> PostModel | None:
        """Удаление записи"""
        logging.info(f"Удаление записи c id {post_id}")

        response = self.delete_object(WordPressURLS.POSTS_DELETE_URL, post_id, delete_data)
        assert response.status_code == 200, "Статус-код ответа неверный"
        post_from_api = get_post_from_api(response.json())

        logging.info(f"Статус-код ответа на запрос удаления записи: {response.status_code}")
        logging.info(f"Результат запроса удаления записи: {post_from_api}")
        return post_from_api
