from django import forms

from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('book_title','author','book_description','uploaded_by','book_date_published','book_average_rating')