from api.base_api import BaseApi
from config.auth_config import AuthConfig


class WordPressApi(BaseApi):
    """Класс, описывающий тестовый сервис, который предоставляет
    точки доступа для управления сущностями через API"""
    def __init__(self):
        self.auth_info = (AuthConfig.USERNAME, AuthConfig.PASSWORD)

    def create_object(self, url: str, data: dict) -> dict:
        """Метод, создающий сущность на сервисе"""
        return self._request_post(expected_status_code = 201, auth=self.auth_info, url=url, json=data)

    def get_object(self, url: str, object_id: int, data: dict = {}) -> dict:
        """Метод, получающий сущность из сервиса"""
        return self._request_get(auth=self.auth_info, url=f"{url}{object_id}", json=data)

    def get_all_objects(self, url: str) -> dict:
        """Метод, получающий все сущности из сервиса"""
        return self._request_get(auth=self.auth_info, url=url)

    def update_object(self, url: str, object_id: int, data: dict) -> dict:
        """Метод, обновляющий сущность на сервисе"""
        return self._request_post(auth=self.auth_info, url=f"{url}{object_id}", json=data)

    def delete_object(self, url: str, object_id: int, data: dict) -> dict:
        """Метод, удаляющий сущность на сервисе"""
        return self._request_delete(auth=self.auth_info, url=f"{url}{object_id}", json=data)
