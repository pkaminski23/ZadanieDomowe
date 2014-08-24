'''
Created on Aug 6, 2014

@author: pawel
'''

from django import forms

class LoginForm(forms.Form):
    login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
if __name__ == '__main__':
    pass