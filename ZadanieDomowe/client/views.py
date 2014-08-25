'''
Created on Aug 22, 2014

@author: pawel
'''
import django
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from menu.models import Menu, Dish
from client.models import Error
from client.forms import ErrorForm
from menu.forms import MenuForm

@login_required
def menu(request):
    ctx = {}
    ctx = {}
    ctx['successes'] = []
    ctx['warnings'] = []
    ctx['infos'] = []
    ctx['dangers'] = []
    ctx['menus'] = Menu.objects.all()
    ctx['top_menu'] = "Client"
    ctx['side_menu'] = "Menu"
    
    paginator = Paginator(ctx['menus'], 4) # Show 25 contacts per page

    page = request.GET.get('page')
#     print "p.count: ", page.count
#     print "p.num_pages: ", page.num_pages
#     print "p.page_range: ", page.page_range
    try:
        ctx['menus_pags'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        ctx['menus_pags'] = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        ctx['menus_pags'] = paginator.page(paginator.num_pages)
    
    return render_to_response('client/menu.html',
            ctx,
            context_instance=RequestContext(request))

@login_required
def error_menu(request, menu_index):
    ctx = {}
    ctx['successes'] = []
    ctx['warnings'] = []
    ctx['infos'] = []
    ctx['dangers'] = []
    ctx['menus'] = Menu.objects.all()
    ctx['top_menu'] = "Client"
    ctx['side_menu'] = "Menu"
    ctx['id'] = menu_index 
    
    menu_record = Menu.objects.get(id=menu_index)
    if request.method == "POST":
        form_save = ErrorForm(request.POST)
        if form_save.is_valid():
            form_save.save()
            ctx['successes'].append("You comment has been added.")
        else:
            print "not ok"
    else:
        form_save = ErrorForm(initial={'menu': menu_index})
    ctx['error_form'] = form_save
    
    return render_to_response('client/menu_errors.html',
            ctx,
            context_instance=RequestContext(request))  

@login_required
def details_menu(request, menu_index):
    ctx = {}
    ctx['successes'] = []
    ctx['warnings'] = []
    ctx['infos'] = []
    ctx['dangers'] = []
    ctx['menu'] = Menu.objects.get(id=menu_index)
    ctx['top_menu'] = "Client"
    ctx['side_menu'] = "Menu"
    ctx['id'] = menu_index
    
    return render_to_response('client/menu_details.html',
            ctx,
            context_instance=RequestContext(request))

if __name__ == '__main__':
    pass