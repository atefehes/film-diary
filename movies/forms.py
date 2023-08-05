from django import forms
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import MovieLog

UserModel = get_user_model()

class SearchForm(forms.Form):
    term = forms.CharField(required=False)


class MovieForm(forms.ModelForm):
    class Meta:
        model = MovieLog
        fields = ["log_time", "seen"]

    def __int__(self, *args, **kwargs):
        super(MovieForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Create"))