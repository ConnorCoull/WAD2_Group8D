from urllib.parse import urlparse
from django.urls import path
from jot import views

app_name = 'jot'

urlpatterns = [

    path('index/', views.index, name='index'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contactus/', views.contactus, name='contactus'),
    path('categories/', views.categories, name='categories'),
    path('surpriseme/', views.surpriseme, name='surpriseme'),
    path('book/', views.book, name='book'),
    #new link added (to test my function...)
    path('addbook/',views.upload_books,name = 'addbook'),
    
]
