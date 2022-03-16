# -*- coding: utf-8 -*-


from django import forms
from django import models
import os,datetime,random

class UploadFileForm(forms.Form):
    class Meta:
        model = models.UploadFileForm
        fields = "_all_"
        
    def clean_pdf_path(self):
        file = self.cleaned_data["pdf_path"]
        ext = file.name.split(".")[-1].lower()
        if ext != "pdf" :
            raise forms.ValidationError(".PDF files only!")
        new_file_name = "%s_%d"%((datetime.datetime.now().strname('%Y%m%d%H%M%S')),random.randrange(100,999))
        file.name = "%d.pdf"%new_file_name
        return file
   # title = forms.CharField(max_length=50)
  #  pdf = forms.FileField()

class MyModel(models.Model):
    # file will be uploaded to database path “uploads/”
    upload = models.FileField(upload_to='uploads/')
