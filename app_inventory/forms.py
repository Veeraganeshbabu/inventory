from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class createuserform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']


class createcustomerform(ModelForm):
    class Meta:
        model = u_type
        fields = '__all__'
        exclude = ['user']