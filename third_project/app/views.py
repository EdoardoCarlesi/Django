from django.shortcuts import render
from app.models import User


def index(request):

    return render(request, 'app/index.html')


def users(request):

    user_list = User.objects.order_by('last_name')
    user_dict = {'users':user_list}

    return render(request, 'app/users.html', context=user_dict)


