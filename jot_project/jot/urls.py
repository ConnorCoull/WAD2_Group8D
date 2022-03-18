
from django.urls import path
from jot import views
from django.conf import settings
from .views import *
#from .views import *

app_name = 'jot'

urlpatterns = [
    path('', views.index, name='index'),
    path('UploadFile/',IndexView.as_view, name = "UploadFile")
]

