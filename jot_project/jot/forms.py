<<<<<<< HEAD
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
=======
from django import forms

from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('book_title',
                  'author',
                  'book_description',
                  'pdf_upload',

                  )
>>>>>>> 506170a8bee247f8375cfe10fe5ef30a71524778
