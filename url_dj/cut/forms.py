from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from cut.models import Url


class UrlsForm(forms.ModelForm):

    user_url = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Enter Url; example https://www.qwe.com"}
        )
    )

    class Meta:
        model = Url
        fields = [
            "user_url",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Save"))
