from fileinput import filename
from math import floor
import random
from django.http import HttpResponseRedirect, FileResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from datetime import datetime
from django.urls import reverse
from .GoogleBookSearchAPI import getRatings
import os
from .models import Book
from .models import User

#call the upload function in Forms
from .forms import BookForm, UserProfileForm#, ReviewForm
from django.conf import settings


from .models import Book, Category, Review
from django.contrib.auth.decorators import login_required

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

def index(request):
    context_dict = {}
    top_books_list = Book.objects.order_by('-book_views')[:10]
    context_dict['top_books_list'] = top_books_list
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'jot/index.html', context=context_dict)

def about(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'jot/about.html', context=context_dict)

def contactus(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'jot/contactus.html', context=context_dict)

def categories(request):
    context_dict = {}
    context_dict['categories'] = Category.objects.order_by('category_name')
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'jot/categories.html', context=context_dict)

def surpriseme(request):
    book_ids = [book.bookID for book in Book.objects.all()]
    random_book = random.randrange(7, max(book_ids))
    print(random_book)
    return redirect(f'/jot/book/{random_book}')

def userpage(request, username):
    context_dict = {}
    try:
        user = User.objects.get(username=username)
        context_dict['user'] = user
    except User.DoesNotExist:
        context_dict['user'] = None

    try:
        context_dict['user_books'] = Book.objects.filter(author=user)
    except Book.DoesNotExist:
        context_dict['user_books'] = None
    
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'jot/userpage.html', context=context_dict)

def book(request, pk):
    context_dict = {
        'star1':'white-star',
        'star2':'white-star',
        'star3':'white-star',
        'star4':'white-star',
        'star5':'white-star',
        }

    try:
        book = Book.objects.get(bookID=pk)
        GoogleBooksApiFeedback = getRatings(book.book_title)

        rating = GoogleBooksApiFeedback[0]
        total_reviews = GoogleBooksApiFeedback[1]

        if total_reviews == 0:
            rating = book.book_average_rating
            total_reviews = book.book_views

        rating = floor(rating+0.5)

        for count in range(rating):
            context_dict['star'+str(count+1)] = 'yellow-star'

        context_dict['book'] = book
        context_dict["total_reviews"] = total_reviews
        context_dict['book_location'] = str(book.pdf_upload)
    except Book.DoesNotExist:
        context_dict['book'] = None

    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'jot/book.html', context=context_dict)

def pdf_view(request, pk):
    book = Book.objects.get(pk=pk)
    filename = str(book.pdf_upload)
    filepath = os.path.join(settings.MEDIA_ROOT, filename)
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def searchresults(request):
    context_dict = {}
    keyword = request.GET.get('query-input')

    if keyword:
            context_dict['users_list'] = User.objects.filter(username__icontains = keyword)
            context_dict['books_list'] = Book.objects.filter(book_title__icontains = keyword)

    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    context_dict['query'] = keyword
    return render(request, 'jot/searchresults.html', context=context_dict)

def category(request, category_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_slug)
        books = Book.objects.filter(book_category=category)
        context_dict['books'] = books
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['books'] = None
        context_dict['category'] = None
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'jot/category.html', context=context_dict)

def review(request, pk):
    context_dict = {}
    try:
        book = Book.objects.get(bookID=pk)
        context_dict['book'] = book
    except Book.DoesNotExist:
        context_dict['book'] = None
    try:
        reviews = Review.objects.get(review_book=pk)
        context_dict['reviews'] = reviews
    except Review.DoesNotExist:
        context_dict['reviews'] = None
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'jot/review.html', context=context_dict)


@login_required
def upload_books(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    if request.method == 'POST' :
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'jot/index.html')
    else:
        form = BookForm()
    context_dict['form'] = form        
    return render(request,'jot/addbook.html',context=context_dict)

@login_required
def addreview(request, pk):
    context_dict = {}

    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        book = None

    if book == None:
        return redirect('/jot/')

    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            if book:
                review = form.save(commit=False)
                review.review_book = book
                review.save()

                return redirect(reverse('jot:book', kwargs={'pk': book.bookID}))

    visitor_cookie_handler(request)
    context_dict = {'form': form, 'book': book}
    context_dict['visits'] = request.session['visits']
    return render(request, 'jot/about.html', context=context_dict) #replace me


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

#def review(request, pk):
    #take a list 

#Matthew: here we allow users to edit their bio, user type and profile pic, email address
#and username cannot be changed, changing password is seperate 
def edit_profile(request):
    if request.method == 'POST' :
        profile_form = UserProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
