from django.shortcuts import render
from . import forms

def index(request):

    return render(request, 'app/index.html')


def form_name_view(request):
    form = forms.FormName()

    print('Form Name View')

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        
        print('POST')

        if form.is_valid():
            print("Validation success!")
            print("Name : ", form.cleaned_data['name'])
            print("Mail : ", form.cleaned_data['email'])
            print("Text : ", form.cleaned_data['text'])

    

    return render(request, 'app/form_page.html', {'form':form})

