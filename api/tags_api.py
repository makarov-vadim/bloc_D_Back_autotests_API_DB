import logging

import allure

from api.wordpress_api import WordPressApi
from config.wordpress_config import WordPressURLS
from helpers.api_helpers import get_tag_from_api
from models.models import TagModel


class TagsApi(WordPressApi):
    """Класс, описывающий создание, обновление и удаление метки на сервисе через API"""
    @allure.step("Создание метки")
    def create_tag(self, tag: TagModel) -> TagModel:
        logging.info(f"Создание метки {tag}")
        response_body = self.create_object(WordPressURLS.TAGS_CREATE_URL, tag.model_dump())
        return get_tag_from_api(response_body)

    @allure.step("Получение метки")
    def retrieve_tag(self, post_id: int) -> TagModel:
        logging.info(f"Получение метки с id {post_id}")
        response_body = self.get_object(WordPressURLS.TAGS_GET_URL, post_id)
        return get_tag_from_api(response_body)

    @allure.step("Обновление метки")
    def update_tag(self, tag_id: int, data: dict) -> TagModel | None:
        logging.info(f"Обновление метки с id {tag_id} и обновляемыми параметрами {data}")
        response_body = self.update_object(WordPressURLS.TAGS_UPDATE_URL, tag_id, data)
        return get_tag_from_api(response_body)

    @allure.step("Удаление метки")
    def delete_tag(self, tag_id: int, delete_data: dict) -> TagModel | None:
        logging.info(f"Удаление метки c id {tag_id}")
        response_body = self.delete_object(WordPressURLS.TAGS_DELETE_URL, tag_id, delete_data)
        return get_tag_from_api(response_body)
