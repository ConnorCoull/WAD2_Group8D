from django.http import HttpResponseRedirect
from django.shortcuts import render
#from .forms import UploadFileForm
from django.db.models import Q
from datetime import datetime
from .models import Book

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

def index(request):
    model = Book
    keyword = request.GET.get('q')
    context_dict = {}
    if keyword:
       books_list = Book.objects.filter(book_title__icontains = keyword)
       context_dict['books_list'] = books_list
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'jot/index.html', context=context_dict)


def about(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'jot/about.html', context=context_dict)

def contactus(request):
    #maybe a dictionary of our information would be useful
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'jot/contactus.html', context=context_dict)

def categories(request):
    #we will need to collect the categories here, this will require a context dict
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'jot/categories.html', context=context_dict)

def surpriseme(request):
    #this will take an argument of a page fetched at random

    #potentually get rid of all of this and in the return return a page.html response??
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'jot/surpriseme.html', context=context_dict)

def book(request):
    #this will take an argument of a page fetched at random

    #potentually get rid of all of this and in the return return a page.html response??
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'jot/book.html', context=context_dict)

# Not a view, this is just a helper function
def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits += 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie

    request.session['visits'] = visits
