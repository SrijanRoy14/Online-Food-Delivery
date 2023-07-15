from django import forms
from . models import *
from django.contrib.auth.models import User
class Menuform(forms.ModelForm):
    class Meta:
        model=MenuItem
        fields='__all__'
    def __init__(self, *args, **kwargs):
            super(Menuform,self).__init__(*args, **kwargs)
            self.fields['category'].empty_label = "Select"
           # self.fields['image'].required = False #to set a field as not required


class orderform(forms.ModelForm):
    class Meta:
        model=ordermodel
        fields='__all__'
    def __init__(self, *args, **kwargs):
            super(orderform,self).__init__(*args, **kwargs)
            self.fields['items'].empty_label = "Select"
           # self.fields['image'].required = False #to set a field as not required


class contactform(forms.ModelForm):
    class Meta:
        model=contact
        fields='__all__'

class admform(forms.ModelForm):
    class Meta:
        model=adminuser
        fields='__all__'

class userform(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'
