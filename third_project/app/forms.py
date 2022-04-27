from django import forms
from app.models import User

class NewUserForm(forms.ModelForm):

    # Add validations here
    class Meta():
        model = User
        fields = '__all__'

