import logging

import allure

from api.wordpress_api import WordPressApi
from config.wordpress_config import WordPressURLS
from helpers.api_helpers import get_category_from_api
from models.models import CategoryModel


class CategoriesApi(WordPressApi):
    """Класс, описывающий создание, обновление и удаление рубрики на сервисе через API"""
    @allure.step("Создание рубрики")
    def create_category(self, category: CategoryModel) -> CategoryModel:
        logging.info(f"Создание рубрики {category}")
        response_body = self.create_object(WordPressURLS.CATEGORIES_CREATE_URL, category.model_dump())
        return get_category_from_api(response_body)

    @allure.step("Получение рубрики")
    def get_category(self, category_id: int) -> CategoryModel:
        logging.info(f"Получение рубрики с id {category_id}")
        response_body = self.get_object(WordPressURLS.CATEGORIES_GET_URL, category_id)
        return get_category_from_api(response_body)

    @allure.step("Обновление рубрики")
    def update_category(self, category_id: int, data: dict) -> CategoryModel | None:
        logging.info(f"Обновление рубрики с id {category_id} и обновляемыми параметрами {data}")
        response_body = self.update_object(WordPressURLS.CATEGORIES_UPDATE_URL, category_id, data)
        return get_category_from_api(response_body)

    @allure.step("Удаление рубрики")
    def delete_category(self, category_id: int, delete_data: dict) -> CategoryModel | None:
        logging.info(f"Удаление рубрики c id {category_id}")
        response_body = self.delete_object(WordPressURLS.CATEGORIES_DELETE_URL, category_id, delete_data)
        return get_category_from_api(response_body)
