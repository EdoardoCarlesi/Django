from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return HttpResponse("Maledetto il Signore Gesu'")

def help(request):

    help_dict = {'help_info':'Help informations here mothafucka'}

    return render(request, 'help/help.html', context = help_dict)

