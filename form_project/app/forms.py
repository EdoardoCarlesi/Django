from django import forms
from django.core import validators


def check_for_cristo(value):
    
    if value.lower() != 'cristo':
        raise forms.ValidationError("Name needs to be Cristo!")

class FormName(forms.Form):

    name = forms.CharField(validators=[check_for_cristo])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)

    # Hidden field
    botcatcher = forms.CharField(required=False, 
                                widget=forms.HiddenInput, 
                                validators=[validators.MaxLengthValidator(0)])


    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError('Gesu Cristo scrivile bene ste mail, devono essere uguali!')
    
    '''
    # no need for this, use djangos built in 
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']

        if len(botcatcher) > 0:
            raise forms.ValidationError("Fuckin' BOT!")
    '''
