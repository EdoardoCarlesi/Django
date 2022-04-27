from django.shortcuts import render


def index(request):
    return render(request, 'app/index.html')

def other(request):
    return render(request, 'app/other.html')

def relative_url(request):
    return render(request, 'app/relative_url.html')

