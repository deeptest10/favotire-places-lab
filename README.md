#Куди піти?

Python version: 3.12.3

Як запустити проект:
Команди виконуються після завантаження репо, з його кореня (Linux / WSL):
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver