from django.shortcuts import render
from app.forms import UserForm, UserProfileInfoForm

from django.urls import reverse
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'app/index.html')

@login_required
def special(request):
    return HttpResponse('Special user only page')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active!') 
        else:

            print('Failed login!')
            print(f'User {username} pwd {password}')
            return HttpResponse('Invalid login') 

    else:
        return render(request, 'app/login.html', {})

def register(request):

    registered = False
    
    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            # Set password method hashes the password
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            try:
                profile.profile_pic = request.FILES['profile_pic']
            except:
                profile.profile_pic = ''

            profile.save()

            registered = True

        # Form is invalid
        else:
            print(user_form.errors, profile_form.errors)

    # This is not a post method
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'app/registration.html', 
            {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})
