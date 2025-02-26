from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ContactMessage

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text','photo']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username','email','password1','password2',)


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage  # Link form to model
        fields = ['name', 'email', 'issue']  # Use all fields from the model
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'issue': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
