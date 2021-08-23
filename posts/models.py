from django.db import models
from django.contrib.auth.models import User
from users.models import Profile

# Create your models here.

# class User(models.Model):
class Test_User(models.Model):

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_admin = models.BooleanField(default=False)

    bio = models.TextField(blank=True)

    birthdate = models.DateField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

class Post(models.Model):

    # If an user is delete, also his posts
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    # The profile is linked too, if there is any situation where is needed
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    # str([app].[model]) avoid making unnecesary relations
    # profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    # Link the Profile rather than the user
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username."""
        return f'{self.title} by @{self.user.username}'
        # return f'{self.title} by @{self.profile.user.username}'