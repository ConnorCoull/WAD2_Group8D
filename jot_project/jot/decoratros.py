from os import access
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import REDIRECT_FIELD_NAME


#MATTHEW: NOT IN USE YET, will be used in future to restrict specific views to authors 
def author_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):

    acc = user_passes_test(
        lambda u: u.user_type, 
        login_url=login_url,
        redirect_field_name=redirect_field_name
    ) 
    if function:
        return acc(function)
    else:
        return acc