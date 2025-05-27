import logging

import allure
import pytest

from helpers.api_helpers import get_user_from_api, get_user_from_bd
from helpers.t_data import TData


@pytest.mark.users
@allure.epic("WordPress_API_Tests")
@allure.feature("Test Suite - Users")
class TestsUsersApi:
    """Класс, описывающий автотест точки доступа Users сервиса WordPress"""
    @allure.story("Тестирование POST-запроса на создание пользователя")
    def test_create_user(self, user, users_service, users_db):
        """Тест-кейс 10. Тестирование POST-запроса на создание пользователя"""
        # Создание пользователя с помощью POST-запроса
        api_response = users_service.create_user(user)
        assert api_response.status_code == 201, "Статус-код ответа неверный"

        # Пользователь из ответа на POST-запроса
        user_from_api = get_user_from_api(api_response.json())

        # Пользователь из БД
        db_response = users_db.get_user(user_from_api.id)
        user_from_db = get_user_from_bd(db_response)

        logging.info(f"User from api response = {user_from_api}")
        logging.info(f"User from DB = {user_from_db}")
        assert user_from_api == user_from_db, "Пользователь, вернувшийся в ответе на POST-запрос не совпадает с пользователем в БД"
        users_db.delete_user(user_from_db.id)


    @allure.story("Тестирование POST-запроса на изменение пользователя")
    def test_update_user(self, users_service, updated_user_data, users_db, user_id):
        """Тест-кейс 11. Тестирование POST-запроса на изменение пользователя"""
        # Пользователь из БД до изменения
        db_response_1 = users_db.get_user(user_id)
        user_from_db_1 = get_user_from_bd(db_response_1)

        # Изменение пользователя с помощью POST-запроса
        api_response = users_service.update_user(user_id, updated_user_data)
        assert api_response.status_code == 200, "Статус-код ответа неверный"

        # Пользователь из ответа на POST-запроса
        user_from_api = get_user_from_api(api_response.json())

        # Пользователь из БД после изменения
        db_response_2 = users_db.get_user(user_id)
        user_from_db_2 = get_user_from_bd(db_response_2)

        logging.info(f"User from DB before update = {user_from_db_1}")
        logging.info(f"User from api response = {user_from_api}")
        logging.info(f"User from DB after update = {user_from_db_2}")

        assert user_from_api != user_from_db_1 and user_from_api == user_from_db_2, "Пользователь не обновлен POST-запросом"


    @allure.story("Тестирование DELETE-запроса на удаление пользователя")
    def test_delete_user(self, users_service, users_db, user_id):
        """Тест-кейс 12. Тестирование DELETE-запроса на удаление пользователя"""
        # Пользователь из БД до удаления
        db_response_1 = users_db.get_user(user_id)
        user_from_db_1 = get_user_from_bd(db_response_1)

        # Удаление пользователя с помощью DELETE-запроса
        api_response = users_service.delete_user(user_id, TData.DELETE_USER_DATA)
        assert api_response.status_code == 200, "Статус-код ответа неверный"

        # Пользователь из БД после удаления. При корректном удалении вернет None
        db_response_2 = users_db.get_user(user_id)
        user_from_db_2 = get_user_from_bd(db_response_2)

        logging.info(f"User from DB before delete = {user_from_db_1}")
        logging.info(f"User from DB after delete = {user_from_db_2}")

        assert user_from_db_2 != user_from_db_1 and user_from_db_2 is None, "Пользователь не удален"
