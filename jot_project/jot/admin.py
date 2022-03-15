from django.contrib import admin
import os 
import django
from jot.models import Users, Book, Review, Admin, UserProfile

admin.site.register(Users)
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Admin)
admin.site.register(UserProfile)
