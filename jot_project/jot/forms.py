# -*- coding: utf-8 -*-


from django import forms
from models import CheckingFileProperties

class UploadFileForm(forms.ModelForm):
    class Meata:
        model = CheckingFileProperties
        fields = "__all__"
        

