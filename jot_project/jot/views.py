from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models import Q
from datetime import datetime
#call the upload function in Forms
from .forms import BookForm
from .models import Book
from django.conf import settings

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

def index(request):

    '''html=
    <from>
        <form role="search" method="get" id="searchform" action="/search/">
            {% url jot:search %}
        <input type="search" name="q" placeholder="lets search!" required>
        <button type="sub">
        <span class=""></span></button>>
    </from>
    
    q = request.GET.get('q')
    error_msg = ''
    if not q:
        error_msg = "input what you want to search"
        return render(request, 'index.html', {'error_msg': error_msg})
    post_list = Post.objects.filter(Q(title_icontains=q)|Q(body__icontains=q))      
    return render(request, 'index.html', {'error_msg': error_msg, 'post_list':post_list}) 
    #if request.method == 'POST':
        #form = UploadFileForm(request.POST, request.FILES)
       # if form.is_valid():
            #handle_uploaded_file(request.FILES['file'])
            #return HttpResponseRedirect('/success/url/')
    #else:
        #form = UploadFileForm()
    #return render(request, 'upload.html', {'form': form})'''

    #context_dict = {'boldmessage': 'Check'}
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'jot/index.html', context=context_dict)
    #return HttpResponse("<h1>JOT</h1><p>I am the homepage!</p>")


def about(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'jot/about.html', context=context_dict)
    #return HttpResponse("<h1>JOT</h1><p>This is the about page</p><a href='/jot/'>Index</a>")

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
#i
#required login?
def upload_files(request):
    if request.method == 'POST' :
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('categories')
        #if upload successed, then return to categories page.(or anyother pages?)
    else:
        form = BookForm()
    return render(request,'jot/addbook.html',{'form':form})
 
