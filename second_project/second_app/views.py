from django.shortcuts import render
from django.http import HttpRequest


def index(request):
    return HttpRequest("<em>Mortacci tua!</em>")