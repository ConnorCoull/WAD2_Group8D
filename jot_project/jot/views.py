from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import View
from .models import CheckingFileProperties
# Create your views here.
def index(request):
    return HttpResponse("<h1>JOT</h1><br /><p>Welcome to jot!</p>")

#@login_required
class IndexView(View):
    def get(self,request):
        return render(request, 'upload/uploadfile.html')
    def post(self,request):
        #get the title and content
        form = CheckingFileProperties(request.POST, request.FILES)
        #send data to dataase
        if form.is_valid():
            form.save()
            return HttpResponse("Success upload!")
        else:
            print(form.errors.get_json_data())
            return HttpResponse("Fail uploaded!")



