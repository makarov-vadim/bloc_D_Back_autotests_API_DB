import logging

import allure

from api.wordpress_api import WordPressApi
from config.wordpress_config import WordPressURLS
from helpers.api_helpers import get_post_from_api
from helpers.t_data import TData
from models.models import PostModel


class PostsApi(WordPressApi):
    """Класс, описывающий создание, обновление и удаление записи на сервисе через API"""
    @allure.step("Создание записи")
    def create_post(self, post: PostModel) -> PostModel:
        logging.info(f"Создание записи {post}")
        response_body = self.create_object(WordPressURLS.POSTS_CREATE_URL, post.model_dump())
        return get_post_from_api(response_body)

    @allure.step("Получение записи")
    def get_post(self, post_id: int) -> PostModel:
        logging.info(f"Получение записи с id {post_id}")
        response_body = self.get_object(WordPressURLS.POSTS_GET_URL, post_id, TData.GET_CONTEXT_DATA)
        return get_post_from_api(response_body)

    @allure.step("Обновление записи")
    def update_post(self, post_id: int, data: dict) -> PostModel | None:
        logging.info(f"Обновление записи с id {post_id} и обновляемыми параметрами {data}")
        response_body = self.update_object(WordPressURLS.POSTS_UPDATE_URL, post_id, data)
        return get_post_from_api(response_body)

    @allure.step("Удаление записи")
    def delete_post(self, post_id: int, delete_data: dict) -> PostModel | None:
        logging.info(f"Удаление записи c id {post_id}")
        response_body = self.delete_object(WordPressURLS.POSTS_DELETE_URL, post_id, delete_data)
        return get_post_from_api(response_body)
