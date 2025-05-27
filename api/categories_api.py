import allure
from requests import Response

from api.wordpress_api import WordPressApi
from config.wordpress_config import WordPressURLS
from models.models import CategoryModel


class CategoriesApi(WordPressApi):
    """Класс, описывающий создание, обновление и удаление рубрики на сервисе через API"""
    @allure.step("Создание рубрики")
    def create_category(self, category: CategoryModel) -> Response:
        """Создание рубрики"""
        return self.create_object(WordPressURLS.CATEGORIES_CREATE_URL, category.model_dump())

    @allure.step("Обновление рубрики")
    def update_category(self, category_id: int, data: dict) -> Response:
        """Обновление рубрики"""
        return self.update_object(WordPressURLS.CATEGORIES_UPDATE_URL, category_id, data)

    @allure.step("Удаление рубрики")
    def delete_category(self, category_id: int, delete_data: dict) -> Response:
        """Удаление рубрики"""
        return self.delete_object(WordPressURLS.CATEGORIES_DELETE_URL, category_id, delete_data)
