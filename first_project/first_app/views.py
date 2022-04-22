from django.shortcuts import render
from django.http import HttpResponse


# Simple response model
def index(request):

    my_dict = {'insert_me':'Maledetto il Signore Gesu Cristo.py'}

    return render(request, 'first_app/index.html', context=my_dict)

