'''
Created on Jul 24, 2014

@author: pawel
'''

import django
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from ZadanieDomowe.forms import LoginForm

def home(request):
    ctx = {}
    ctx = {}
    ctx['successes'] = []
    ctx['warnings'] = []
    ctx['infos'] = []
    ctx['dangers'] = []
    ctx['top_menu'] = "Home"
    ctx['side_menu'] = ""
    
    return render_to_response('ZadanieDomowe/home.html',
            ctx,
            context_instance=RequestContext(request))
    
def login_user(request):
    ctx = {}
    ctx['successes'] = []
    ctx['warnings'] = []
    ctx['infos'] = []
    ctx['dangers'] = []
    ctx['top_menu'] = "Home"
    ctx['side_menu'] = "login"
    
    if request.method == 'POST':
        # dane z POST
        form = LoginForm(request.POST)
        if form.is_valid():
            print 'ok'
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(username=login, password=password)
            if user is not None:
                django.contrib.auth.login(request, user)
                # zalogowany
                print "logged"
                return HttpResponseRedirect('home/')
            else:
                # blad
                print "not logged"
                pass
            # dane poprawne
            pass
        else:
            print "not ok news"
            # dane niepoprawne
            pass
    else:
        # formularz
        form = LoginForm()
    
    ctx['form'] = form
    return render_to_response('ZadanieDomowe/login.html',
            ctx,
            context_instance=RequestContext(request))
    
def logout_user(request):
    ctx = {}
    ctx['successes'] = []
    ctx['warnings'] = []
    ctx['infos'] = []
    ctx['dangers'] = []
    ctx['top_menu'] = "Home"
    ctx['side_menu'] = "Logout"
    
    logout(request)
    return render_to_response('ZadanieDomowe/logout.html',
            ctx,
            context_instance=RequestContext(request))

def about(request):
    ctx = {}
    ctx = {}
    ctx['successes'] = []
    ctx['warnings'] = []
    ctx['infos'] = []
    ctx['dangers'] = []
    ctx['top_menu'] = "Home"
    ctx['side_menu'] = "About"
    
    return render_to_response('ZadanieDomowe/about.html',
            ctx,
            context_instance=RequestContext(request))

if __name__ == '__main__':
    pass