##### 1) Клонировать проект

    git clone https://github.com/Silicone-Team/DocTour-Api

##### 2) Создать venv и активироать если ее нет

    Windows:
    python -m venv venv
    cd venv/Scripts/activate

    linux and Mac:
    source venv/bin/activate
    

##### 3) Скачать зависимости

    pip install -r requirements.txt

##### 4) Создать и заполнить .env

    Пока что только "TOKEN" и "DEBUG" 

##### 5) Не забудь миграции

    python manage.py migrate

##### 6) Используй часто "black" в терминале для PEP-8

    black .

Если будут проблемы или трудности пишите в группу :)