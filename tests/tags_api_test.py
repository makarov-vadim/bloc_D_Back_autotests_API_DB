import logging

import allure
import pytest

from helpers.api_helpers import get_tag_from_api, get_tag_from_bd
from helpers.t_data import TData


@pytest.mark.tags
@allure.epic("WordPress_API_Tests")
@allure.feature("Test Suite - Tags")
class TestsTagsApi:
    """Класс, описывающий автотест точки доступа Tags сервиса WordPress"""
    @allure.story("Тестирование POST-запроса на создание метки")
    def test_create_tag(self, tag, tags_service, tags_db):
        """Тест-кейс 07. Тестирование POST-запроса на создание метки"""
        # Создание метки с помощью POST-запроса
        api_response = tags_service.create_tag(tag)
        assert api_response.status_code == 201, "Статус-код ответа неверный"

        # Метка из ответа на POST-запроса
        tag_from_api = get_tag_from_api(api_response.json())

        # Метка из БД
        db_response = tags_db.get_tag(tag_from_api.id)
        tag_from_db = get_tag_from_bd(db_response)

        logging.info(f"Tag from api response = {tag_from_api}")
        logging.info(f"Tag from DB = {tag_from_db}")
        assert tag_from_api == tag_from_db, "Метка, вернувшаяся в ответе на POST-запрос не совпадает с меткой в БД"
        tags_db.delete_tag(tag_from_db.id)


    @allure.story("Тестирование POST-запроса на изменение метки")
    def test_update_tag(self, tags_service, updated_tag_data, tags_db, tag_id):
        """Тест-кейс 08. Тестирование POST-запроса на изменение метки"""
        # Метка из БД до изменения
        db_response_1 = tags_db.get_tag(tag_id)
        tag_from_db_1 = get_tag_from_bd(db_response_1)

        # Изменение метки с помощью POST-запроса
        api_response = tags_service.update_tag(tag_id, updated_tag_data)
        assert api_response.status_code == 200, "Статус-код ответа неверный"

        # Метка из ответа на POST-запроса
        tag_from_api = get_tag_from_api(api_response.json())

        # Метка из БД после изменения
        db_response_2 = tags_db.get_tag(tag_id)
        tag_from_db_2 = get_tag_from_bd(db_response_2)

        logging.info(f"Tag from DB before update = {tag_from_db_1}")
        logging.info(f"Tag from api response = {tag_from_api}")
        logging.info(f"Tag from DB after update = {tag_from_db_2}")

        assert tag_from_api != tag_from_db_1 and tag_from_api == tag_from_db_2, "Метка не обновлена POST-запросом"


    @allure.story("Тестирование DELETE-запроса на удаление метки")
    def test_delete_tag(self, tags_service, tags_db, tag_id):
        """Тест-кейс 09. Тестирование DELETE-запроса на удаление метки"""
        # Метка из БД до удаления
        db_response_1 = tags_db.get_tag(tag_id)
        tag_from_db_1 = get_tag_from_bd(db_response_1)

        # Удаление метки с помощью DELETE-запроса
        api_response = tags_service.delete_tag(tag_id, TData.DELETE_DATA)
        assert api_response.status_code == 200, "Статус-код ответа неверный"

        # Метка из БД после удаления. При корректном удалении вернет None
        db_response_2 = tags_db.get_tag(tag_id)
        tag_from_db_2 = get_tag_from_bd(db_response_2)

        logging.info(f"Tag from DB before delete = {tag_from_db_1}")
        logging.info(f"Tag from DB after delete = {tag_from_db_2}")

        assert tag_from_db_2 != tag_from_db_1 and tag_from_db_2 is None, "Метка не удалена"
