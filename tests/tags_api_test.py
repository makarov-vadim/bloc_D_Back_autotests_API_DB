import allure
import pytest

from helpers.t_data import TData


@pytest.mark.tags
@allure.epic("WordPress_API_Tests")
class TestsTagsApi:
    """Класс, описывающий автотест точки доступа Tags сервиса WordPress"""
    @allure.id("7")
    @allure.title("Создание метки")
    def test_create_tag(self, tag, tags_service, tags_db):
        tag_from_api = tags_service.create_tag(tag)
        tag_from_db = tags_db.get_tag(tag_from_api.id)

        assert tag_from_api == tag_from_db, "Метка, вернувшаяся в ответе на POST-запрос не совпадает с меткой в БД"
        tags_db.delete_tag(tag_from_db.id)


    @allure.id("8")
    @allure.title("Изменение метки")
    def test_update_tag(self, tags_service, updated_tag_data, tags_db, tag_id):
        tag_from_db_1 = tags_db.get_tag(tag_id)
        tag_from_api = tags_service.update_tag(tag_id, updated_tag_data)
        tag_from_db_2 = tags_db.get_tag(tag_id)

        assert tag_from_api != tag_from_db_1 and tag_from_api == tag_from_db_2, "Метка не обновлена POST-запросом"


    @allure.id("9")
    @allure.title("Удаление метки")
    def test_delete_tag(self, tags_service, tags_db, tag_id):
        tag_from_db_1 = tags_db.get_tag(tag_id)
        tag_from_api = tags_service.delete_tag(tag_id, TData.DELETE_DATA)
        tag_from_db_2 = tags_db.get_tag(tag_id)

        assert tag_from_db_2 != tag_from_db_1 and tag_from_db_2 is None, "Метка не удалена"
