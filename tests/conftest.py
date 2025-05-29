import logging

import pytest
from faker import Faker

from api.categories_api import CategoriesApi
from api.posts_api import PostsApi
from api.tags_api import TagsApi
from api.users_api import UsersApi
from databases.categories_db import CategoriesDB
from databases.posts_db import PostsDB
from databases.tags_db import TagsDB
from databases.users_db import UsersDB
from helpers.api_helpers import get_category, get_post, get_tag, get_user


# Фикстуры API сервисов
@pytest.fixture(scope="session")
def posts_service():
    yield PostsApi()

@pytest.fixture(scope="session")
def categories_service():
    yield CategoriesApi()

@pytest.fixture(scope="session")
def tags_service():
    yield TagsApi()

@pytest.fixture(scope="session")
def users_service():
    yield UsersApi()


# Фикстуры БД
@pytest.fixture(scope="session")
def posts_db():
    yield PostsDB()

@pytest.fixture(scope="session")
def categories_db():
    yield CategoriesDB()

@pytest.fixture(scope="session")
def tags_db():
    yield TagsDB()

@pytest.fixture(scope="session")
def users_db():
    yield UsersDB()

@pytest.fixture(scope="session")
def fake():
    yield Faker("ru_RU")


# Фикстуры тестовых данных
@pytest.fixture(scope="function")
def new_post_data(fake):
    post_content = fake.text()
    post_title = fake.name()
    new_post_data = {
            "title": post_title,
            "content": post_content,
            "status": "publish"
        }
    logging.info(f"Тестовые данные для новой записи: {new_post_data}")
    yield new_post_data

@pytest.fixture(scope="function")
def updated_post_data(fake):
    updated_post_data = {"content": fake.text()}
    logging.info(f"Тестовые данные для обновления записи: {updated_post_data}")
    yield updated_post_data

@pytest.fixture(scope="function")
def new_category_data(fake):
    new_category_data = {"name": fake.job()}
    logging.info(f"Тестовые данные для новой рубрики: {new_category_data}")
    yield new_category_data

@pytest.fixture(scope="function")
def updated_category_data(fake):
    updated_category_data = {"name": fake.job()}
    logging.info(f"Тестовые данные для обновления рубрики: {updated_category_data}")
    yield updated_category_data

@pytest.fixture(scope="function")
def new_tag_data(fake):
    new_tag_data = {"name": fake.company()}
    logging.info(f"Тестовые данные для новой метки: {new_tag_data}")
    yield new_tag_data

@pytest.fixture(scope="function")
def updated_tag_data(fake):
    updated_tag_data = {"name": fake.company()}
    logging.info(f"Тестовые данные для обновления метки: {updated_tag_data}")
    yield updated_tag_data

@pytest.fixture(scope="function")
def new_user_data(fake):
    new_user_data = {
        "username": fake.user_name(),
        "email": fake.email(),
        "password": f"{fake.password()}"
    }
    logging.info(f"Тестовые данные для нового пользователя: {new_user_data}")
    yield new_user_data

@pytest.fixture(scope="function")
def updated_user_data(fake):
    updated_user_data = {"email": fake.email()}
    logging.info(f"Тестовые данные для обновления пользователя: {updated_user_data}")
    yield updated_user_data


# Фикстуры сущностей как моделей
@pytest.fixture(scope="function")
def post(new_post_data):
    yield get_post(new_post_data)

@pytest.fixture(scope="function")
def category(new_category_data):
    yield get_category(new_category_data)

@pytest.fixture(scope="function")
def tag(new_tag_data):
    yield get_tag(new_tag_data)

@pytest.fixture(scope="function")
def user(new_user_data):
    yield get_user(new_user_data)


# Фикстуры сущностей в БД
@pytest.fixture(scope="function")
def post_id(post, posts_db):
    post_id = posts_db.create_post(post)
    yield post_id
    posts_db.delete_post(post_id)

@pytest.fixture(scope="function")
def category_id(category, categories_db):
    category_id = categories_db.create_category(category)
    yield category_id
    categories_db.delete_category(category_id)

@pytest.fixture(scope="function")
def tag_id(tag, tags_db):
    tag_id = tags_db.create_tag(tag)
    yield tag_id
    tags_db.delete_tag(tag_id)

@pytest.fixture(scope="function")
def user_id(user, users_db):
    user_id = users_db.create_user(user)
    yield user_id
    users_db.delete_user(user_id)
