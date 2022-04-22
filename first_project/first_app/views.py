from django.shortcuts import render
from django.http import HttpResponse


# Simple response model
def index(request):
    return HttpResponse("Madonna Cana!")


