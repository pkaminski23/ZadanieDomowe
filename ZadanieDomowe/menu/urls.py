'''
Created on Aug 22, 2014

@author: pawel
'''
from django.conf.urls import patterns, include, url

urlpatterns = patterns('menu.views',
    # Examples:
    url(r'^$', 'index'),
    url(r'^index', 'index'),
    url(r'^menu', 'menu'),
    url(r'^add_menu', 'add_menu'),
    url(r'^edit_menu/(\d+)/$', 'edit_menu'),
    url(r'^delete_menu/(\d+)/$', 'delete_menu'),
    
    url(r'^dishes', 'dishes'),
    url(r'^add_dish', 'add_dish'),
    url(r'^edit_dish/(\d+)/$', 'edit_dish'),
    url(r'^delete_dish/(\d+)/$', 'delete_dish'),
    url(r'^clients_errors/$', 'clients_errors'),
    
    url(r'^delete_error/(\d+)/$', 'delete_error'),
)

if __name__ == '__main__':
    pass