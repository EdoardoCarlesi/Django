from django.shortcuts import render
from . import forms

def index(request):

    return render(request, 'app/index.html')


def form_name_view(request):
    form = forms.FormName()

    return render(request, 'app/form_page.html', {'form':form})

