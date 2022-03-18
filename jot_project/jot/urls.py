from urllib.parse import urlparse
from django.urls import path
from jot import views

app_name = 'jot'

urlpatterns = [
    path('search/', views.search, name='search'),
]
