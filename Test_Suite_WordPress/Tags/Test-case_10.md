# Тест-кейс 10. Получение метки

## Описание
Позитивный тест на получение метки по ее id.

## Автор: Макаров Вадим Михайлович

## Предусловия
1) Используется базовая аутентификация согласно 
[документации](https://developer.wordpress.org/rest-api/using-the-rest-api/authentication/#basic-authentication-with-application-passwords)
с параметрами USERNAME и PASSWORD, Роль - Администратор (далее - Параметры аутентификации)
2) Доступны для чтения таблицы wp_terms и wp_term_taxonomy из базы данных wordpress (далее - БД)
3) В БД существует метка с параметрами: id = {id}; name = "TagName"; taxonomy = "post_tag"


## Шаги
Выполнить GET-запрос http://localhost:8000/index.php?rest_route=/wp/v2/tags/{id} , используя Параметры аутентификации


## Ожидаемый результат
1) Получен статус-код ответа 200 OK
2) Тело ответа содержит параметры: id = {id}; name = "TagName"; taxonomy = "post_tag"
