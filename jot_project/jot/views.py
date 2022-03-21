from django.http import HttpResponseRedirect
from django.shortcuts import render
#from .forms import UploadFileForm
from django.db.models import Q

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

def index(request):

    html='''
    <from>
        <form role="search" method="get" id="searchform" action="/search/">
            {% url jot:search %}
        <input type="search" name="q" placeholder="lets search!" required>
        <button type="sub">
        <span class=""></span></button>>
    </from>
    '''
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
    #return render(request, 'upload.html', {'form': form})

    #context_dict = {'boldmessage': 'Check'}
    return render(request, 'jot/index.html')
    #return HttpResponse("<h1>JOT</h1><p>I am the homepage!</p>")


def about(request):
    #context_dict = {'boldmessage': 'This is the boldmessage for the About page!'}
    return render(request, 'jot/about.html')
    #return HttpResponse("<h1>JOT</h1><p>This is the about page</p><a href='/jot/'>Index</a>")

