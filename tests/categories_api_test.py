import allure
import pytest

from helpers.t_data import TData


@pytest.mark.categories
@allure.epic("WordPress_API_Tests")
class TestsCategoriesApi:
    """Класс, описывающий автотест точки доступа Categories сервиса WordPress"""
    @allure.id("5")
    @allure.title("Создание рубрики")
    def test_create_category(self, category, categories_service, categories_db):
        category_from_api = categories_service.create_category(category)
        category_from_db = categories_db.get_category(category_from_api.id)

        assert category_from_api == category_from_db, "Рубрика, вернувшаяся в ответе на POST-запрос не совпадает с рубрикой в БД"
        categories_db.delete_category(category_from_db.id)


    @allure.id("6")
    @allure.title("Получение рубрики")
    def test_get_category(self, categories_service, categories_db, category_id):
        category_from_db = categories_db.get_category(category_id)
        category_from_api = categories_service.get_category(category_id)

        assert category_from_api == category_from_db, "Полученная рубрика не совпадает с рубрикой в БД"


    @allure.id("7")
    @allure.title("Изменение рубрики")
    def test_update_category(self, categories_service, updated_category_data, categories_db, category_id):
        category_from_db_1 = categories_db.get_category(category_id)
        category_from_api = categories_service.update_category(category_id, updated_category_data)
        category_from_db_2 = categories_db.get_category(category_id)

        assert category_from_api != category_from_db_1 and category_from_api == category_from_db_2, "Рубрика не обновлена POST-запросом"


    @allure.id("8")
    @allure.title("Удаление рубрики")
    def test_delete_category(self, categories_service, categories_db, category_id):
        category_from_db_1 = categories_db.get_category(category_id)
        category_from_api = categories_service.delete_category(category_id, TData.DELETE_DATA)
        category_from_db_2 = categories_db.get_category(category_id)

        assert category_from_db_2 != category_from_db_1 and category_from_db_2 is None, "Рубрика не удалена"
