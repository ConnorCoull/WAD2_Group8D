from django import forms 
from django.contrib.auth.models import User
from jot.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'user_email', 'user_password','user_type')
    
    class UserProfileForm(forms.ModelForm):
        class Meta:
            model = UserProfile
            fields = ('bio', 'user_picture',)