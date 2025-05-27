import logging

import allure
import pytest

from helpers.api_helpers import get_category_from_api, get_category_from_db
from helpers.t_data import TData


@pytest.mark.categories
@allure.epic("WordPress_API_Tests")
@allure.feature("Test Suite - Categories")
class TestsCategoriesApi:
    """Класс, описывающий автотест точки доступа Categories сервиса WordPress"""
    @allure.story("Тестирование POST-запроса на создание рубрики")
    def test_create_category(self, category, categories_service, categories_db):
        """Тест-кейс 04. Тестирование POST-запроса на создание рубрики"""
        # Создание рубрики с помощью POST-запроса
        api_response = categories_service.create_category(category)
        assert api_response.status_code == 201, "Статус-код ответа неверный"

        # Рубрика из ответа на POST-запроса
        category_from_api = get_category_from_api(api_response.json())

        # Рубрика из БД
        db_response = categories_db.get_category(category_from_api.id)
        category_from_db = get_category_from_db(db_response)


        logging.info(f"Category from api response = {category_from_api}")
        logging.info(f"Category from DB = {category_from_db}")
        assert category_from_api == category_from_db, "Рубрика, вернувшаяся в ответе на POST-запрос не совпадает с рубрикой в БД"
        categories_db.delete_category(category_from_db.id)


    @allure.story("Тестирование POST-запроса на изменение рубрики")
    def test_update_category(self, categories_service, updated_category_data, categories_db, category_id):
        """Тест-кейс 05. Тестирование POST-запроса на изменение рубрики"""
        # Рубрика из БД до изменения
        db_response_1 = categories_db.get_category(category_id)
        category_from_db_1 = get_category_from_db(db_response_1)

        # Изменение рубрики с помощью POST-запроса
        api_response = categories_service.update_category(category_id, updated_category_data)
        assert api_response.status_code == 200, "Статус-код ответа неверный"

        # Рубрика из ответа на POST-запроса
        category_from_api = get_category_from_api(api_response.json())

        # Рубрика из БД после изменения
        db_response_2 = categories_db.get_category(category_id)
        category_from_db_2 = get_category_from_db(db_response_2)

        logging.info(f"Category from DB before update = {category_from_db_1}")
        logging.info(f"Category from api response = {category_from_api}")
        logging.info(f"Category from DB after update = {category_from_db_2}")

        assert category_from_api != category_from_db_1 and category_from_api == category_from_db_2, "Рубрика не обновлена POST-запросом"


    @allure.story("Тестирование DELETE-запроса на удаление рубрики")
    def test_delete_category(self, categories_service, categories_db, category_id):
        """Тест-кейс 06. Тестирование DELETE-запроса на удаление рубрики"""
        # Рубрика из БД до удаления
        db_response_1 = categories_db.get_category(category_id)
        category_from_db_1 = get_category_from_db(db_response_1)

        # Удаление рубрики с помощью DELETE-запроса
        api_response = categories_service.delete_category(category_id, TData.DELETE_DATA)
        assert api_response.status_code == 200, "Статус-код ответа неверный"

        # Рубрика из БД после удаления. При корректном удалении вернет None
        db_response_2 = categories_db.get_category(category_id)
        category_from_db_2 = get_category_from_db(db_response_2)

        logging.info(f"Category from DB before delete = {category_from_db_1}")
        logging.info(f"Category from DB after delete = {category_from_db_2}")

        assert category_from_db_2 != category_from_db_1 and category_from_db_2 is None, "Рубрика не удалена"
