from pydantic import BaseModel
from typing import Optional

class PostModel(BaseModel):
    """Класс, описывающий модель записи"""
    id: Optional[int] = None
    title: str
    content: str
    status: str

class CategoryModel(BaseModel):
    """Класс, описывающий модель рубрики"""
    id: Optional[int] = None
    name: str
    taxonomy: str = "category"


class TagModel(BaseModel):
    """Класс, описывающий модель метки"""
    id: Optional[int] = None
    name: str
    taxonomy: str = "post_tag"


class UserModel(BaseModel):
    """Класс, описывающий модель пользователя"""
    id: Optional[int] = None
    username: str
    email: str
    password: Optional[str] = None
