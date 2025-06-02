from typing import Optional

from pydantic import BaseModel


class WordPressBaseModel(BaseModel):
    """Класс, описывающий базовую модель для сервиса WordPress"""
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            self_dump = {k: v for k, v in self.model_dump().items() if k not in ("id", "password")}
            other_dump = {k: v for k, v in other.model_dump().items() if k not in ("id", "password")}

            return self_dump == other_dump
        return NotImplemented


class PostModel(WordPressBaseModel):
    """Класс, описывающий модель записи"""
    id: Optional[int] = None
    title: str
    content: str
    status: str


class CategoryModel(WordPressBaseModel):
    """Класс, описывающий модель рубрики"""
    id: Optional[int] = None
    name: str
    taxonomy: str = "category"


class TagModel(WordPressBaseModel):
    """Класс, описывающий модель метки"""
    id: Optional[int] = None
    name: str
    taxonomy: str = "post_tag"


class UserModel(WordPressBaseModel):
    """Класс, описывающий модель пользователя"""
    id: Optional[int] = None
    username: str
    email: str
    password: Optional[str] = None
