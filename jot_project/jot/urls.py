from urllib.parse import urlparse
from django.urls import path
from jot import views

app_name = 'jot'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/',views.upload_file, name = 'upload',),
]
