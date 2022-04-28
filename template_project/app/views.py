from django.shortcuts import render


def index(request):

    context_dict = {'text':'Lambderto Dini', 'number':'166'}

    return render(request, 'app/index.html', context_dict)

def other(request):
    return render(request, 'app/other.html')

def relative_url(request):
    return render(request, 'app/relative_url.html')

