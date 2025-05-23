import pytest
from databases.wordpress_db import WordPressDB
from api.wordpress_api import WordPressApi
from helpers.api_helpers import get_post, get_category, get_tag, get_user
from helpers.t_data import TData


@pytest.fixture(scope="session")
def service_db():
    service_db = WordPressDB()
    service_db.delete_all_data()
    yield service_db
    service_db.delete_all_data()

@pytest.fixture(scope="session")
def service():
    service = WordPressApi()
    yield service

@pytest.fixture(scope="function")
def post_id(service_db):
    post = get_post(TData.NEW_POST_DATA)
    post_id = service_db.create_post(post)
    yield post_id
    service_db.delete_post(post_id)

@pytest.fixture(scope="function")
def category_id(service_db):
    category = get_category(TData.NEW_CATEGORY_DATA)
    category_id = service_db.create_category(category)
    yield category_id
    service_db.delete_category(category_id)

@pytest.fixture(scope="function")
def tag_id(service_db):
    tag = get_tag(TData.NEW_TAG_DATA)
    tag_id = service_db.create_tag(tag)
    yield tag_id
    service_db.delete_tag(tag_id)

@pytest.fixture(scope="function")
def user_id(service_db):
    user = get_user(TData.NEW_USER_DATA)
    user_id = service_db.create_user(user)
    yield user_id
    service_db.delete_user(user_id)
