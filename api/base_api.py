import logging

import requests


class BaseApi:
    """Класс, описывающий базовый сервис, который предоставляет
    точки доступа для управления сущностями через API"""

    def _request_post(self, expected_status_code=200, **kwargs) -> dict:
        """Метод, создающий/обновляющий сущность на сервисе"""
        response = requests.post(**kwargs)
        self._assert_status_code(response.status_code, expected_status_code)
        response_body = response.json()

        logging.info(f"Тело ответа на POST-запрос: {response_body}")
        return response_body

    def _request_get(self, expected_status_code=200, **kwargs) -> dict:
        """Метод, получающий сущность из сервиса"""
        response = requests.get(**kwargs)
        self._assert_status_code(response.status_code, expected_status_code)
        response_body = response.json()

        logging.info(f"Тело ответа на GET-запрос: {response_body}")
        return response_body

    def _request_delete(self, expected_status_code=200, **kwargs) -> dict:
        """Метод, удаляющий сущность на сервисе"""
        response = requests.delete(**kwargs)
        self._assert_status_code(response.status_code, expected_status_code)
        response_body = response.json()

        logging.info(f"Тело ответа на DELETE-запрос: {response_body}")
        return response_body

    def _assert_status_code(self, status_code: int, expected_status_code: int) -> None:
        assert status_code == expected_status_code, "Статус-код ответа неверный"
        logging.info(f"Статус-код ответа: {status_code}")
