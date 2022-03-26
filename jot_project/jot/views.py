from math import floor
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models import Q
from datetime import datetime
from .GoogleBookSearchAPI import getRatings

#call the upload function in Forms
from .forms import BookForm, UserProfileForm
from django.conf import settings

from .models import Book
from .models import Users

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

def index(request):
    context_dict = {}
    top_books_list = Book.objects.order_by('-book_views')[:10]
    context_dict['top_books_list'] = top_books_list

    keyword = request.GET.get('query-input')
    chosen_category = request.GET.get('chosen-category')

    if keyword:
        if chosen_category == "user":
            context_dict['users_list'] = Users.objects.filter(username__icontains = keyword)
            
        elif chosen_category == "book":
            context_dict['books_list'] = Book.objects.filter(book_title__icontains = keyword)

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

def book(request, pk):
    #may need to take a random book

    context_dict = {
        'star1':'white-star',
        'star2':'white-star',
        'star3':'white-star',
        'star4':'white-star',
        'star5':'white-star',}

    try:
        book = Book.objects.get(bookID=pk)
        GoogleBooksApiFeedback = getRatings(book.book_title) #grab this from the book data/ api

        rating = GoogleBooksApiFeedback[0]
        rating = floor(rating+0.5)

        for count in range(rating):
            context_dict['star'+str(count+1)] = 'yellow-star'

        context_dict['book'] = book
        context_dict["total_reviews"] = GoogleBooksApiFeedback[1]
    except Book.DoesNotExist:
        context_dict['book'] = None

    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'jot/book.html', context=context_dict)

def searchresults(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'jot/searchresults.html', context=context_dict)

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
  
    
# If anyone want to change the page after uploading successfully, modify return redirect('index') 
@login_required
def upload_books(request):
    if request.method == 'POST' :
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm()
        
    return render(request,'jot/addbook.html',{'form': form})

#Matthew: here we alow users to edit thier bio, user type and proficle pic, email adress
#and usernmae cannot be changed, chaging password is seperate 
def edit_profile(request):
    if request.method == 'POST' :
        profile_form = UserProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()