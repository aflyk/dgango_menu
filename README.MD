# Джанго меню
Приложение позволяющее создавать древовидное меню.   
Используются следующие технологии:    
1 django-mptt(работа с древовидными моделями)   
2 templatetags (регистрация функции для вызова ее из темплейта)   
3 poetry (альтернатива venv)
# Работа с проектом
Склонируйте проект  
```
git clone https://github.com/aflyk/django_menu.git
```  
Перейдите в каталог с проектом  
```
cd django_menu 
```
Активируйте окружение   
```
poetry install
poetry shell
```
Выполните миграции
```
python manage.py migrate
```
Создайте супер пользователя
```
python manage.py createsuperuser
```
Запустите сервер
```
python manage.py runserver
```
Админка для заполнение полей находится по адресу  
```
localhost/admin 
```
name = mainmenu, его можно менять в файле
```
menu/templates/menu/menu.html
{% draw_menu 'mainmenu'%} # за место mainmenu любое другое имя
```
Посмотреть меню можно по адресу
```
localhost/menu
```


# Структура проекта

.  
├── manage.py  
├── menu  
│   ├── admin.py  
│   ├── apps.py  
│   ├── __init__.py  
│   ├── migrations  
│   │   ├── 0001_initial.py  
│   │   ├── 0002_menuitem_display_name.py  
│   │   ├── __init__.py  
│   │       ├── 0001_initial.cpython-38.pyc  
│   │       ├── 0002_menuitem_display_name.cpython-38.pyc  
│   │       └── __init__.cpython-38.pyc  
│   ├── models.py  
│   ├── templates  
│   │   ├── home.html  
│   │   └── menu  
│   │       └── menu.html  
│   ├── templatetags  
│   │   ├── __init__.py  
│   │   ├── menu_tags.py  
│   │   ├── __init__.cpython-38.pyc  
│   │       └── menu_tags.cpython-38.pyc  
│   ├── tests.py  
│   ├── urls.py  
│   └── views.py  
├── menuapp  
│   ├── asgi.py  
│   ├── __init__.py  
│   ├── settings.py  
│   ├── urls.py  
│   └── wsgi.py  
├── poetry.lock  
├── pyproject.toml  
├── README.MD  
└── templates  
    └── base.html  

