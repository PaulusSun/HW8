# HW8**Задание. Напишите автотесты на методы приложения x-clients.** 

- [GET] /employee
- [POST] /employee
- [GET] /employee/{id}
- [PATCH] /employee/{id}

**Требования:**

- тесты должны работать с библиотекой `pytest`
- тесты должны использовать библиотеку `requests`
- тесты должны быть стабильны:
    - их не нужно редактировать перед каждым запуском
    - повторный запуск теста приводит к тому же статусу
- тесты должны быть 2х видов:
    - позитивные
    - проверяющие обязательность полей
    Обязательность полей можно узнать в Swagger

🤓если сервис не получает запросы 30 минут, он выключается. Первое обращение к сервису потребует больше времени (около 2 минут), т.к. сервис запускается заново. Учитывайте это при работе.

**Swagger:** [https://x-clients-be.onrender.com/docs/](https://x-clients-be.onrender.com/docs/)

**URL приложения:** [https://x-clients-be.onrender.com](https://x-clients-be.onrender.com)

**Для авторизации:** 

- запрос принимается по адресу /auth/login
- вам потребуется логин и пароль. Можно использовать любую пару:
