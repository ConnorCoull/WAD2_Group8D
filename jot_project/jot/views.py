from django.shortcuts import render
from django.http import HttpResponse
from .forms import ModelFormWithFileField
from somewhere import handle_uploaded_file
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    return HttpResponse("<h1>JOT</h1><br /><p>Welcome to jot!</p>")

def upload_file(request):
    if request.method == 'POST':
        form = ModelFormWithFileField(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect("SUCCESS")
    else:
        form = ModelFormWithFileField()
    return render(request, 'upload/uploadfiles.html', {'form': form})
