# Тест-кейс 02. Редактирование записи

## Описание
Позитивный тест на редактирование записи (изменение параметра title).

## Автор: Макаров Вадим Михайлович

## Предусловия
1) Используется базовая аутентификация согласно 
[документации](https://developer.wordpress.org/rest-api/using-the-rest-api/authentication/#basic-authentication-with-application-passwords)
с параметрами USERNAME и PASSWORD, Роль - Администратор (далее - Параметры аутентификации)
2) Тело запроса: {"title": "The new title"} (далее - Тело запроса)
3) Доступна для чтения таблица wp_posts из базы данных wordpress (далее - БД)
4) В БД существует запись с параметрами: id = {id}; post_title = "The title for the post"; post_content = "The content for the post", post_status = "publish"


## Шаги
Выполнить POST-запрос http://localhost:8000/index.php?rest_route=/wp/v2/posts/{id} , используя Параметры аутентификации и Тело запроса


## Ожидаемый результат
1) Получен статус-код ответа 200 OK
2) Тело ответа содержит параметры: id = {id}; title = "The new title"; content = "The content for the post", status = "publish" (далее - Обновленные параметры)
3) В БД существует запись с Обновленными параметрами