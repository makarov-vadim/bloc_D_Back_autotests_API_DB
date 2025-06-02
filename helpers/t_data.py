class TData:
    NEW_POST_DATA = {
            "title": "The title for the post",
            "content": "The content for the post",
            "status": "publish"
        }
    NEW_CATEGORY_DATA = {
        "name": "CategoryName"
    }
    NEW_TAG_DATA = {
        "name": "TagName"
    }
    NEW_USER_DATA = {
        "username": "UserName",
        "email": "user_email@mail.ru",
        "password": f"{hash("qwerty_123")}"
    }

    UPDATED_POST_DATA = {"title": "The new title"}
    UPDATED_CATEGORY_DATA = {"name": "NewCategoryName"}
    UPDATED_TAG_DATA = {"name": "NewTagName"}
    UPDATED_USER_DATA = {"email": "new_user_email@mail.ru"}

    DELETE_DATA = {"force": True}
    DELETE_USER_DATA = {"force": True, "reassign": 1}
    GET_CONTEXT_DATA = {"context": "edit"}
