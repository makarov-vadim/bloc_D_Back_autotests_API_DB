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
        """Создание рубрики"""
        logging.info(f"Создание рубрики {category}")

        response = self.create_object(WordPressURLS.CATEGORIES_CREATE_URL, category.model_dump())
        assert response.status_code == 201, "Статус-код ответа неверный"
        category_from_api = get_category_from_api(response.json())

        logging.info(f"Статус-код ответа на запрос создания рубрики: {response.status_code}")
        logging.info(f"Результат запроса создания рубрики: {category_from_api}")
        return category_from_api


    @allure.step("Обновление рубрики")
    def update_category(self, category_id: int, data: dict) -> CategoryModel | None:
        """Обновление рубрики"""
        logging.info(f"Обновление рубрики с id {category_id} и обновляемыми параметрами {data}")

        response = self.update_object(WordPressURLS.CATEGORIES_UPDATE_URL, category_id, data)
        assert response.status_code == 200, "Статус-код ответа неверный"
        category_from_api = get_category_from_api(response.json())

        logging.info(f"Статус-код ответа на запрос обновления рубрики: {response.status_code}")
        logging.info(f"Результат запроса обновления рубрики: {category_from_api}")
        return category_from_api


    @allure.step("Удаление рубрики")
    def delete_category(self, category_id: int, delete_data: dict) -> CategoryModel | None:
        """Удаление рубрики"""
        logging.info(f"Удаление рубрики c id {category_id}")

        response = self.delete_object(WordPressURLS.CATEGORIES_DELETE_URL, category_id, delete_data)
        assert response.status_code == 200, "Статус-код ответа неверный"
        category_from_api = get_category_from_api(response.json())

        logging.info(f"Статус-код ответа на запрос удаления рубрики: {response.status_code}")
        logging.info(f"Результат запроса удаления рубрики: {category_from_api}")
        return category_from_api
