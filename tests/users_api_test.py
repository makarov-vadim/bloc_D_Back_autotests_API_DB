import allure
import pytest

from helpers.t_data import TData


@pytest.mark.users
@allure.epic("WordPress_API_Tests")
class TestsUsersApi:
    """Класс, описывающий автотест точки доступа Users сервиса WordPress"""
    @allure.id("10")
    @allure.title("Создание пользователя")
    def test_create_user(self, user, users_service, users_db):
        """Тест-кейс 10. Тестирование POST-запроса на создание пользователя"""
        user_from_api = users_service.create_user(user)
        user_from_db = users_db.get_user(user_from_api.id)

        assert user_from_api == user_from_db, "Пользователь, вернувшийся в ответе на POST-запрос не совпадает с пользователем в БД"
        users_db.delete_user(user_from_db.id)


    @allure.id("11")
    @allure.title("Изменение пользователя")
    def test_update_user(self, users_service, updated_user_data, users_db, user_id):
        """Тест-кейс 11. Тестирование POST-запроса на изменение пользователя"""
        user_from_db_1 = users_db.get_user(user_id)
        user_from_api = users_service.update_user(user_id, updated_user_data)
        user_from_db_2 = users_db.get_user(user_id)

        assert user_from_api != user_from_db_1 and user_from_api == user_from_db_2, "Пользователь не обновлен POST-запросом"


    @allure.id("12")
    @allure.title("Удаление пользователя")
    def test_delete_user(self, users_service, users_db, user_id):
        """Тест-кейс 12. Тестирование DELETE-запроса на удаление пользователя"""
        user_from_db_1 = users_db.get_user(user_id)
        user_from_api = users_service.delete_user(user_id, TData.DELETE_USER_DATA)
        user_from_db_2 = users_db.get_user(user_id)

        assert user_from_db_2 != user_from_db_1 and user_from_db_2 is None, "Пользователь не удален"
