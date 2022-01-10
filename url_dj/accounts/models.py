from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to="users_images", blank=True)


class UserProfile(models.Model):
    """Creating user model in order to have data stored into db"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.user.username
