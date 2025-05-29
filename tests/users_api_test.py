import allure
import pytest

from helpers.t_data import TData


@pytest.mark.users
@allure.epic("WordPress_API_Tests")
class TestsUsersApi:
    """Класс, описывающий автотест точки доступа Users сервиса WordPress"""
    @allure.id("13")
    @allure.title("Создание пользователя")
    def test_create_user(self, user, users_service, users_db):
        user_from_api = users_service.create_user(user)
        user_from_db = users_db.get_user(user_from_api.id)

        assert user_from_api == user_from_db, "Пользователь, вернувшийся в ответе на POST-запрос не совпадает с пользователем в БД"
        users_db.delete_user(user_from_db.id)


    @allure.id("14")
    @allure.title("Получение пользователя")
    def test_retrieve_user(self, users_service, users_db, user_id):
        user_from_db = users_db.get_user(user_id)
        user_from_api = users_service.retrieve_user(user_id)

        assert user_from_api == user_from_db, "Полученный пользователь не совпадает с пользователем в БД"


    @allure.id("15")
    @allure.title("Изменение пользователя")
    def test_update_user(self, users_service, updated_user_data, users_db, user_id):
        user_from_db_1 = users_db.get_user(user_id)
        user_from_api = users_service.update_user(user_id, updated_user_data)
        user_from_db_2 = users_db.get_user(user_id)

        assert user_from_api != user_from_db_1 and user_from_api == user_from_db_2, "Пользователь не обновлен POST-запросом"


    @allure.id("16")
    @allure.title("Удаление пользователя")
    def test_delete_user(self, users_service, users_db, user_id):
        user_from_db_1 = users_db.get_user(user_id)
        user_from_api = users_service.delete_user(user_id, TData.DELETE_USER_DATA)
        user_from_db_2 = users_db.get_user(user_id)

        assert user_from_db_2 != user_from_db_1 and user_from_db_2 is None, "Пользователь не удален"
