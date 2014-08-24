'''
Created on Aug 22, 2014

@author: pawel
'''

from django.forms import ModelForm
from django import forms
from models import Error
from menu.models import Menu

class ErrorForm(ModelForm):
    class Meta:
        model = Error
        fields = ['data', 'email', 'menu']
        widgets = {
            'data': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
             'menu': forms.Select(attrs={'class': 'form-control', 'readonly':'readonly'})
        }

if __name__ == '__main__':
    pass