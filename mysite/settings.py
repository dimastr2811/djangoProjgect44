import os

# Определение корневой директории проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Настройка базы данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Указываем MySQL
        'NAME': 'mysite_db',                   # Имя базы данных
        'USER': 'mysite_usr',                  # Имя пользователя
        'PASSWORD': 'mysite_pass',             # Пароль
        'HOST': 'localhost',                   # Адрес сервера базы данных
        'PORT': '3306',                        # Порт (по умолчанию 3306)
    }
}
