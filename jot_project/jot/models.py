from django.db import models
from django.core import validators

# Create your models here.
class CheckingFileProperties(models.Model):
    title = models.CharField(max_length=(40))
    content = models.TextField()
    myfile = models.FileField(upload_to="media/%Y/%m/%d",
                              validators=[validators.FileExtensionValidator(['pdf'],
                                                                            message = 'you can only upload .pdf file!')])
