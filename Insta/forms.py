from django import forms 
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from Insta.models import MyInstaUser


# forms defined here handles user inputs

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyInstaUser
        fields = ('username', 'email', 'profile_pic')