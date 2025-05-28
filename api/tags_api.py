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
        """Создание метки"""
        logging.info(f"Создание метки {tag}")

        response = self.create_object(WordPressURLS.TAGS_CREATE_URL, tag.model_dump())
        assert response.status_code == 201, "Статус-код ответа неверный"
        tag_from_api = get_tag_from_api(response.json())

        logging.info(f"Статус-код ответа на запрос создания метки: {response.status_code}")
        logging.info(f"Результат запроса создания метки: {tag_from_api}")
        return tag_from_api


    @allure.step("Обновление метки")
    def update_tag(self, tag_id: int, data: dict) -> TagModel | None:
        """Обновление метки"""
        logging.info(f"Обновление метки с id {tag_id} и обновляемыми параметрами {data}")

        response = self.update_object(WordPressURLS.TAGS_UPDATE_URL, tag_id, data)
        assert response.status_code == 200, "Статус-код ответа неверный"
        tag_from_api = get_tag_from_api(response.json())

        logging.info(f"Статус-код ответа на запрос обновления метки: {response.status_code}")
        logging.info(f"Результат запроса обновления метки: {tag_from_api}")
        return tag_from_api


    @allure.step("Удаление метки")
    def delete_tag(self, tag_id: int, delete_data: dict) -> TagModel | None:
        """Удаление метки"""
        logging.info(f"Удаление метки c id {tag_id}")

        response = self.delete_object(WordPressURLS.TAGS_DELETE_URL, tag_id, delete_data)
        assert response.status_code == 200, "Статус-код ответа неверный"
        tag_from_api = get_tag_from_api(response.json())

        logging.info(f"Статус-код ответа на запрос удаления метки: {response.status_code}")
        logging.info(f"Результат запроса удаления метки: {tag_from_api}")
        return tag_from_api
