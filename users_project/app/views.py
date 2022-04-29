from django.shortcuts import render
from app.forms import UserForm, UserProfileInfoForm


def index(request):
    return render(request, 'app/index.html')


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
