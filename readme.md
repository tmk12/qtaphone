.\env\Scripts\activate
python manage.py runserver


python manage.py shell
->
from django.contrib.auth.models import User
user = User.objects.create_user('nazwa_użytkownika', 'email@example.com', 'hasło')
user.save()

