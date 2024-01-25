## Трекер полезных привычек.
### В рамках учебного курсового проекта реализуйте бэкенд-часть SPA веб-приложения.

Контекст
В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек. Заказчик прочитал книгу, впечатлился и обратился к вам с запросом реализовать трекер полезных привычек.

### Курсовая работа № 7. DRF

#### Критерии приемки курсовой работы
    - Настроили CORS.
    - Настроили интеграцию с Telegram.
    - Реализовали пагинацию.
    - Использовали переменные окружения.
    - Все необходимые модели описаны или переопределены.
    - Все необходимые эндпоинты реализовали.
    - Настроили все необходимые валидаторы.
    - Описанные права доступа заложены.
    - Настроили отложенную задачу через Celery.
    - Проект покрыли тестами как минимум на 80%.
    - Код оформили в соответствии с лучшими практиками.
    - Имеется список зависимостей.

### 1. Для запуска приложения необходимо настроить виртуальное окружение и установить все необходимые зависимости с помощью команд:
    Команда для Windows:
        - python -m venv venv
        - venv\Scripts\activate
        - pip install -r requirement.txt

    Команда для Unix:
        - python3 -m venv venv
        - source venv/bin/activate 
        - pip install -r requirement.txt

### 2. Для запуска redis:
    Redis официально не поддерживается в Windows: 
        - Установите WSL2, Ubuntu. Подробности смотрите тут https://redis.io/docs/getting-started/installation/install-redis-on-windows/
        - sudo apt-get update (обновление)
        - sudo service redis-server start
        - redis-cli
        - Проверка работает ли сервер Redis: введите Ping, ответ от сервера: Pong
        - в IDE через командну строку установите redis: pip install redis

    Команда для Unix:
        - redis-cli

### 3. Для запуска celery:
    Команда для Windows:
        - при указании обработчика событий необходимо добавить флаг -P eventlet
        - celery -A config worker -l INFO -P eventlet
        - celery -A my_project beat —loglevel=info

    Команда для Unix:
        - celery -A config worker --loglevel=info
        - celery -A my_project beat —loglevel=info

### 4. Для заполнения моделей данными необходимо выполнить следующую команду: 
    Команда для Windows:
        - python manage.py fill

    Команда для Unix:
        - python3 manage.py fill

### 5. Для работы с переменными окружениями необходимо заполнить файл
    - env.examples

### 6. Для создания администратора (createsuperuser)
    - заполните поля email, PASSWORD. users/management/commands/csu.py
    - python manage.py csu (Windows)
    - python3 manage.py csu (Unix)

### 7. Для запуска приложения: 
    Команда для Windows:
    - python manage.py runserver

    Команда для Unix:
    - python3 manage.py runserver

### Документация проекта: http://127.0.0.1:8000/swagger/
