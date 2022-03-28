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
    path('book/<int:pk>', views.book, name='book'),
    path('searchresults/', views.searchresults, name='searchresults'),
    path('addbook/',views.upload_books,name = 'addbook'),
    path('book/pdf/<int:pk>/', views.pdf_view, name='pdf'),
    path('category/<slug:category_slug>/', views.category, name='category'),
    path('userpage/<slug:username>', views.userpage, name='userpage'),
    path('book/<int:pk>/review', views.review, name='review'),
    path('book/<int:pk>/addreview', views.addreview, name='addreview'),

]
