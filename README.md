### Проект по Django REST Framework

## часть проверка 


 poetry init
 poetry add --group lint flake8
 poetry add --group lint mypy
 poetry add --group lint black
 poetry add --group lint isort
 # не забыть про .gitignore
 black .         
 isort .   
 flake8 .  
 mypy .     
 requests init    

## часть первая  "Вьюсеты и дженерики"

pip install django 
python -m pip install os   
python -m pip install psycopg2-binary
python -m pip install Pillow
pip install python-dotenv    
pip install dotenv
pip install django-filter   


## часть вторая  "Права доступа в DRF"
Шаг 1. Установка и настройка библиотеки

Установите библиотеку 
djangorestframework-simplejwt
 с помощью pip: 
pip install djangorestframework-simplejwt
.
Добавьте 
rest_framework_simplejwt
 в список установленных приложений 
INSTALLED_APPS
 в файле 
settings.py
 вашего проекта.
