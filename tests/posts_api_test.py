import logging

import allure
import pytest

from helpers.api_helpers import get_post_from_api, get_post_from_db
from helpers.t_data import TData


@pytest.mark.posts
@allure.epic("WordPress_API_Tests")
@allure.feature("Test Suite - Posts")
class TestsPostsApi:
    """Класс, описывающий автотест точки доступа Posts сервиса WordPress"""
    @allure.story("Тестирование POST-запроса на создание записи")
    def test_create_post(self, post, posts_service, posts_db):
        """Тест-кейс 01. Тестирование POST-запроса на создание записи"""
        # Создание записи с помощью POST-запроса
        api_response = posts_service.create_post(post)
        assert api_response.status_code == 201, "Статус-код ответа неверный"

        # Запись из ответа на POST-запроса
        post_from_api = get_post_from_api(api_response.json())

        # Запись из БД
        db_response = posts_db.get_post(post_from_api.id)
        post_from_db = get_post_from_db(db_response)

        logging.info(f"Post from api response = {post_from_api}")
        logging.info(f"Post from DB = {post_from_db}")
        assert post_from_api == post_from_db, "Запись, вернувшаяся в ответе на POST-запрос не совпадает с записью в БД"
        posts_db.delete_post(post_from_db.id)


    @allure.story("Тестирование POST-запроса на изменение записи")
    def test_update_post(self, posts_service, updated_post_data, posts_db, post_id):
        """Тест-кейс 02. Тестирование POST-запроса на изменение записи"""
        # Запись из БД до изменения
        db_response_1 = posts_db.get_post(post_id)
        post_from_db_1 = get_post_from_db(db_response_1)

        # Изменение записи с помощью POST-запроса
        api_response = posts_service.update_post(post_id, updated_post_data)
        assert api_response.status_code == 200, "Статус-код ответа неверный"

        # Запись из ответа на POST-запроса
        post_from_api = get_post_from_api(api_response.json())

        # Запись из БД после изменения
        db_response_2 = posts_db.get_post(post_id)
        post_from_db_2 = get_post_from_db(db_response_2)

        logging.info(f"Post from DB before update = {post_from_db_1}")
        logging.info(f"Post from api response = {post_from_api}")
        logging.info(f"Post from DB after update = {post_from_db_2}")

        assert post_from_api != post_from_db_1 and post_from_api == post_from_db_2, "Запись не обновлена POST-запросом"


    @allure.story("Тестирование DELETE-запроса на удаление записи")
    def test_delete_post(self, posts_service, posts_db, post_id):
        """Тест-кейс 03. Тестирование DELETE-запроса на удаление записи"""
        # Запись из БД до удаления
        db_response_1 = posts_db.get_post(post_id)
        post_from_db_1 = get_post_from_db(db_response_1)

        # Удаление записи с помощью DELETE-запроса
        api_response = posts_service.delete_post(post_id, TData.DELETE_DATA)
        assert api_response.status_code == 200, "Статус-код ответа неверный"

        # Запись из БД после удаления. При корректном удалении вернет None
        db_response_2 = posts_db.get_post(post_id)
        post_from_db_2 = get_post_from_db(db_response_2)

        logging.info(f"Post from DB before delete = {post_from_db_1}")
        logging.info(f"Post from DB after delete = {post_from_db_2}")

        assert post_from_db_2 != post_from_db_1 and post_from_db_2 is None, "Запись не удалена"
