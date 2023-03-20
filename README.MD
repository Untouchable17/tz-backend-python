<h1 align="center">Техническое задание</h1>

<h3 align="center">Процесс установки:</h3>

> Метод 1: Ручная установка

1. Склонируйте репозиторий
```
git clone https://github.com/Untouchable17/tz-backend-python.git
```
2. Создайте и активируйте виртуальное окружение
```
python -m venv venv
source venv/bin/activate
```
3. Установите все зависимости
```
pip install requirements.txt
```
4. Запустите миграции
```
python manage.py makemigrations
python manage.py migrate
```
5. Запустите приложение
```
python manage.py runserver
```
<br/>

> Метод 2: С помощью докера
1. Склонируйте репозиторий
```
git clone https://github.com/Untouchable17/tz-backend-python.git
```
2. Запустите докер
```
docker-compose up --build
```
3. Для создания суперпользователя
```
docker-compose run --rm web sh -c "python manage.py createsuperuser"

```
<br/>

> В качестве СУБД можно поставить и postgresql
1. В settings.py замените содержимое константы DATABASES на:
```
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("POSTGRES_ENGINE"),
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
    }
}
```
2. В файле .env укажите правильные заполните следующие поля:
```
POSTGRES_ENGINE=
POSTGRES_HOST=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
POSTGRES_PORT=
```


## Contact Developer


    Telegram:           @secdet17
    Group:              t.me/secdet_team
    Email:              tylerblackout17@gmail.com
