from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

from accounts.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from cut.models import Url


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("index"))
    else:
        form = UserLoginForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Done!")
            return HttpResponseRedirect(reverse("accounts:login"))
    else:
        form = UserRegistrationForm()
    context = {"form": form}
    return render(request, "accounts/register.html", context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("index"))


@login_required
def profile(request):
    if request.method == "POST":
        form = UserProfileForm(data=request.POST, instance=request.user)
    form = UserProfileForm(instance=request.user)
    urls = Url.objects.filter(user=request.user)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("accounts:profile"))
    return render(request, "accounts/profile.html", {"form": form, "urls": urls})
