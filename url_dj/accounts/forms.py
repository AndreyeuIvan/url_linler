from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
)
from django import forms

from accounts.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter name"})
    )
    password = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter password"})
    )

    class Meta:
        model = User
        fields = ("username", "password")

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control py-4"


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter  name"})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter last name"})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter name of a user"})
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={"placeholder": "Enter an email"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Enter a passcode"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm the passcode"})
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control py-4"


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"readonly": True})
    )
    email = forms.CharField(widget=forms.EmailInput(
        attrs={"readonly": True})
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter  name"})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter last name"})
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
        )

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control py-4"
