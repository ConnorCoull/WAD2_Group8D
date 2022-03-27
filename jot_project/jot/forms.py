#from dataclasses import field
from django import forms 
from django.contrib.auth.models import User
from jot.models import UserProfile,Book,Review

#might not need this, check how registration is interacting with models 
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    
class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('bio', 'user_picture',)

#Do i need to add the book being reviewed and the user reviewing it as a hidden field?
class ReviewFrom(forms.ModelForm):
    review_content  = forms.CharField(max_length=250)
    #Maybe radio buttons insted 
    review_rating = forms.IntegerField()
    class Meta:
        model = Review
        fields = ('review_rating','review_content')
    
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('book_title',
                  'author',
                  'book_description',
                  'pdf_upload',

                  )
