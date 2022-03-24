from django.contrib import admin
import os 
import django
from jot.models import Users, Book, Review, Category

class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'user_type')

class BookAdmin(admin.ModelAdmin):
    list_display = ('book_title', 'book_category', 'author')

class ReviewAdmin(admin.ModelAdmin):
    list_display=('reviewer', 'review_book', 'review_content')


admin.site.register(Users, UsersAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Category)