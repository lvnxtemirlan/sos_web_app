from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Picture, Card, Sender


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text="Optional.")
    last_name = forms.CharField(max_length=30, required=False, help_text="Optional.")
    email = forms.EmailField(
        max_length=254, help_text="Required. Inform a valid email address."
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


class PictureForm(forms.ModelForm):
    user_id = forms.IntegerField()

    class Meta:
        model = Picture
        fields = ['user_id', 'relation', 'image']


class CardForm(forms.ModelForm):
    user_id = forms.IntegerField()

    class Meta:
        model = Card
        fields = ["user_id", "card_first_name", "card_last_name", "card_phone_number", "card_region", "relation"]


class ServiceForm(forms.ModelForm):
    user_id = forms.CharField()
    service_id = forms.CharField()
    relation = forms.CharField()

    class Meta:
        model = Sender
        fields = ["user_id", "service_id", "relation"]