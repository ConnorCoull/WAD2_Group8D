from django import forms 
from django.contrib.auth.models import User
from jot.models import UserProfile,Book

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio', 'user_picture',)


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('book_title',
                  'author',
                  'book_description',
                  'pdf_upload',

                  )
