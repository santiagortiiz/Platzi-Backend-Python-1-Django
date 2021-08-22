from django.contrib.auth.models import User

u = User.objects.create_user(username='santiago', password='admin123')