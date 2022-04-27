from django.shortcuts import render
from app.models import User
from app.forms import NewUserForm


def index(request):

    return render(request, 'app/index.html')


def users(request):

    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            # This is taking you back to the home page
            return index(request)
        else:
            print('ErrorFormInvalid.')

    return render(request, 'app/users.html', {'form':form})


def users_old(request):

    user_list = User.objects.order_by('last_name')
    user_dict = {'users':user_list}

    return render(request, 'app/users.html', context=user_dict)


