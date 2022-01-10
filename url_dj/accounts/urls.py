from django.urls import path
from accounts.views import login, register, logout, profile

app_name = "accounts"


urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("profile/", profile, name="profile"),
    path("logout/", logout, name="logout"),
]
