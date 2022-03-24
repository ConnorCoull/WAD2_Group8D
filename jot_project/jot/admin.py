from django.contrib import admin
import os 
import django
from jot.models import Users, Book, Review, Admin, UserProfile, Category



class BookAdmin(admin.ModelAdmin):
    list_display = ('book_title', 'book_category', 'author')





admin.site.register(Users)
admin.site.register(Book, BookAdmin)
admin.site.register(Review)
admin.site.register(Admin)
admin.site.register(UserProfile)
admin.site.register(Category)