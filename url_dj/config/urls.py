"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required

from cut.views import UrlCreateView, get_url, UrlListView, error_page

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", login_required(UrlCreateView.as_view(), login_url=""), name="index"),
    path("short_url/<int:id>", get_url, name="detail"),
    path("list/", UrlListView.as_view(), name="list"),
    path('error/', error_page, name='error'),
    path("accounts/", include("accounts.urls"), name="accounts"),
]
