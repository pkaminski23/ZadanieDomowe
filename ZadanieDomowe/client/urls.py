'''
Created on Aug 22, 2014

@author: pawel
'''
from django.conf.urls import patterns, include, url

urlpatterns = patterns('client.views',
    # Examples:
    url(r'^$', 'menu'),
    url(r'^menu', 'menu'),
    url(r'^error_menu/(\d+)/$', 'error_menu'),
    url(r'^details_menu/(\d+)/$', 'details_menu'),
)

if __name__ == '__main__':
    pass