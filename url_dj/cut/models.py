from django.db import models
from django.urls import reverse

from accounts.models import User


class Url(models.Model):
    user_url = models.URLField(max_length=5000)
    short_url = models.URLField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_url

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})
