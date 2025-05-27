import allure
from requests import Response

from api.wordpress_api import WordPressApi
from config.wordpress_config import WordPressURLS
from models.models import TagModel


class TagsApi(WordPressApi):
    """Класс, описывающий создание, обновление и удаление метки на сервисе через API"""
    @allure.step("Создание метки")
    def create_tag(self, tag: TagModel) -> Response:
        """Создание метки"""
        return self.create_object(WordPressURLS.TAGS_CREATE_URL, tag.model_dump())

    @allure.step("Обновление метки")
    def update_tag(self, tag_id: int, data: dict) -> Response:
        """Обновление метки"""
        return self.update_object(WordPressURLS.TAGS_UPDATE_URL, tag_id, data)

    @allure.step("Удаление метки")
    def delete_tag(self, tag_id: int, delete_data: dict) -> Response:
        """Удаление метки"""
        return self.delete_object(WordPressURLS.TAGS_DELETE_URL, tag_id, delete_data)

