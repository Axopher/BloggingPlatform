from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'Firstname'}))

    last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'Lastname'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'id':'Email'}))

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) <= 3:
            raise forms.ValidationError('Username must be longer than 3 characters.')
        return username

    def __init__(self,*args,**kwargs):
        super(SignUpForm,self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['id'] = 'Username'
        self.fields['password1'].widget.attrs['id'] = 'Password1'
        self.fields['password2'].widget.attrs['id'] = 'Password2'   