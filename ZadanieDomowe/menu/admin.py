'''
Created on Aug 22, 2014

@author: pawel
'''

from django.contrib import admin

from menu.models import *

admin.site.register(Dish)
admin.site.register(Menu)

if __name__ == '__main__':
    pass