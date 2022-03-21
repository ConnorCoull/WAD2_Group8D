from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #context_dict = {'boldmessage': 'Check'}
    return render(request, 'jot/index.html')
    #return HttpResponse("<h1>JOT</h1><p>I am the homepage!</p>")


def about(request):
    #context_dict = {'boldmessage': 'This is the boldmessage for the About page!'}
    return render(request, 'jot/about.html')
    #return HttpResponse("<h1>JOT</h1><p>This is the about page</p><a href='/jot/'>Index</a>")