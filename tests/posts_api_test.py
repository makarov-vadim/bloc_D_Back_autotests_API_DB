import allure
import pytest

from helpers.t_data import TData


@pytest.mark.posts
@allure.epic("WordPress_API_Tests")
class TestsPostsApi:
    """Класс, описывающий автотест точки доступа Posts сервиса WordPress"""
    @allure.id("1")
    @allure.title("Создание записи")
    def test_create_post(self, post, posts_service, posts_db):
        post_from_api = posts_service.create_post(post)
        post_from_db = posts_db.get_post(post_from_api.id)

        assert post_from_api == post_from_db, "Запись, вернувшаяся в ответе на POST-запрос не совпадает с записью в БД"
        posts_db.delete_post(post_from_db.id)


    @allure.id("2")
    @allure.title("Получение записи")
    def test_get_post(self, posts_service, post, post_id):
        post_from_api = posts_service.get_post(post_id)

        assert post_from_api == post, "Запись, полученная из GET-запроса не соответствует сгенерированной"


    @allure.id("3")
    @allure.title("Изменение записи")
    def test_update_post(self, posts_service, updated_post_data, posts_db, post_id):
        post_from_db_1 = posts_db.get_post(post_id)
        post_from_api = posts_service.update_post(post_id, updated_post_data)
        post_from_db_2 = posts_db.get_post(post_id)

        assert post_from_api != post_from_db_1 and post_from_api == post_from_db_2, "Запись не обновлена POST-запросом"


    @allure.id("4")
    @allure.title("Удаление записи")
    def test_delete_post(self, posts_service, posts_db, post_id):
        post_from_db_1 = posts_db.get_post(post_id)
        post_from_api = posts_service.delete_post(post_id, TData.DELETE_DATA)
        post_from_db_2 = posts_db.get_post(post_id)

        assert post_from_db_2 != post_from_db_1 and post_from_db_2 is None, "Запись не удалена"
