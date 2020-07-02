from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length = 20,
        widget = forms.TextInput(attrs = {'class':'form-control mb-30'}))
    phone_number = forms.CharField(max_length=13, 
        widget = forms.TextInput(attrs = {'class':'form-control mb-30', 'placeholder' : '+998991112233'}))
    password1 = forms.CharField(max_length = 40,
        widget = forms.PasswordInput(attrs = {'class':'form-control mb-30'}))
    password2 = forms.CharField(max_length = 40,
        widget = forms.PasswordInput(attrs = {'class':'form-control mb-30'}))
    class Meta:
        model = CustomUser
        fields = ('username', 'phone_number')
    

class CustomLoginForm(forms.Form):
    username = forms.CharField(max_length = 20,
        widget = forms.TextInput(attrs = {'class':'form-control mb-30'}))
    password = forms.CharField(max_length = 40,
        widget = forms.PasswordInput(attrs = {'class':'form-control mb-30'}))
    

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'phone_number')


