import allure
import pytest

from helpers.t_data import TData
from helpers.api_helpers import get_user, get_user_from_api, get_user_from_bd

@pytest.mark.users
@allure.epic("WordPress_API_Tests")
@allure.feature("Test Suite - Users")
class TestsUsersApi:
    """Класс, описывающий автотест точки доступа Users сервиса WordPress"""
    @allure.story("Тестирование POST-запроса на создание пользователя")
    def test_create_user(self, service, service_db):
        """Тест-кейс 10. Тестирование POST-запроса на создание пользователя"""
        # Создание пользователя с помощью POST-запроса
        new_user = get_user(TData.NEW_USER_DATA)
        api_response = service.create_user(new_user)
        assert api_response.status_code == 201, "Статус-код ответа неверный"

        # Пользователь из ответа на POST-запроса
        user_from_api = get_user_from_api(api_response.json())

        # Пользователь из БД
        db_response = service_db.get_user(user_from_api.id)
        user_from_db = get_user_from_bd(db_response)

        print()
        print(f"User from api response = {user_from_api}")
        print(f"User from DB = {user_from_db}")
        assert user_from_api == user_from_db, "Пользователь, вернувшийся в ответе на POST-запрос не совпадает с пользователем в БД"


    @allure.story("Тестирование POST-запроса на изменение пользователя")
    def test_update_user(self, service, service_db, user_id):
        """Тест-кейс 11. Тестирование POST-запроса на изменение пользователя"""
        # Пользователь из БД до изменения
        db_response_1 = service_db.get_user(user_id)
        user_from_db_1 = get_user_from_bd(db_response_1)

        # Изменение пользователя с помощью POST-запроса
        api_response = service.update_user(user_id, TData.UPDATED_USER_DATA)
        assert api_response.status_code == 200, "Статус-код ответа неверный"

        # Пользователь из ответа на POST-запроса
        user_from_api = get_user_from_api(api_response.json())

        # Пользователь из БД после изменения
        db_response_2 = service_db.get_user(user_id)
        user_from_db_2 = get_user_from_bd(db_response_2)

        print()
        print(f"User from DB before update = {user_from_db_1}")
        print(f"User from api response = {user_from_api}")
        print(f"User from DB after update = {user_from_db_2}")

        assert user_from_api != user_from_db_1 and user_from_api == user_from_db_2, "Пользователь не обновлен POST-запросом"


    @allure.story("Тестирование DELETE-запроса на удаление пользователя")
    def test_delete_user(self, service, service_db, user_id):
        """Тест-кейс 12. Тестирование DELETE-запроса на удаление пользователя"""
        # Пользователь из БД до удаления
        db_response_1 = service_db.get_user(user_id)
        user_from_db_1 = get_user_from_bd(db_response_1)

        # Удаление пользователя с помощью DELETE-запроса
        api_response = service.delete_user(user_id, TData.DELETE_USER_DATA)
        assert api_response.status_code == 200, "Статус-код ответа неверный"

        # Пользователь из БД после удаления. При корректном удалении вернет None
        db_response_2 = service_db.get_user(user_id)
        user_from_db_2 = get_user_from_bd(db_response_2)

        print()
        print(f"User from DB before delete = {user_from_db_1}")
        print(f"User from DB after delete = {user_from_db_2}")

        assert user_from_db_2 != user_from_db_1 and user_from_db_2 is None, "Пользователь не удален"
