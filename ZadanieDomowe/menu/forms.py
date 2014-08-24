'''
Created on Aug 22, 2014

@author: pawel
'''

from django.forms import ModelForm
from django import forms
from models import Dish
from models import Menu

class TestForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()

class DishForm(ModelForm):
    #picture = forms.ImageField(required=False)
    #picture.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = Dish
        fields = ['name', 'price', 'picture']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'picture': forms.FileInput()
        }
        
        
class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'dishes']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dishes': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

if __name__ == '__main__':
    pass