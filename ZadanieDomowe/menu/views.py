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
from django.contrib.auth.decorators import user_passes_test

from menu.models import Menu, Dish
from client.models import Error
from forms import MenuForm, DishForm
from django.db.models import Count

@login_required
@user_passes_test(lambda u: u.is_superuser)
def index(request):
    ctx = {}
    ctx = {}
    ctx['successes'] = []
    ctx['warnings'] = []
    ctx['infos'] = []
    ctx['dangers'] = []
    ctx['top_menu'] = "Menu"
    ctx['side_menu'] = ""
    
    return render_to_response('menu/home.html',
            ctx,
            context_instance=RequestContext(request))
    
@login_required
@user_passes_test(lambda u: u.is_superuser)
def menu(request):
    ctx = {}
    ctx = {}
    ctx['successes'] = []
    ctx['warnings'] = []
    ctx['infos'] = []
    ctx['dangers'] = []
    ctx['top_menu'] = "Menu"
    ctx['side_menu'] = "Menu"
    ctx['sort'] = request.GET.get('sort')
    ctx['page_number'] = request.GET.get('page')
    
    sort = ctx['sort']
    print "sort: ", sort
    if sort == "name":
        ctx['menus'] = Menu.objects.extra(
                                          select={'lower_name': 'lower(name)'}).order_by('lower_name')
    elif sort == "number":
        ctx['menus'] = Menu.objects.annotate(num_dishes=Count('dishes')) \
                .order_by('-num_dishes')
    else:
        ctx['menus'] = Menu.objects.order_by('id')
    paginator = Paginator(ctx['menus'], 5) # Show 5 menus per page

    page = ctx['page_number']
#     print "p.count: ", page.count
#     print "p.num_pages: ", page.num_pages
#     print "p.page_range: ", page.page_range
    try:
        ctx['menus_pags'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        ctx['menus_pags'] = paginator.page(1)
        ctx['page_number'] = 1
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        ctx['menus_pags'] = paginator.page(paginator.num_pages)
        ctx['page_number'] = paginator.num_pages
    
    return render_to_response('menu/menu.html',
            ctx,
            context_instance=RequestContext(request))

@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_menu(request):
    ctx = {}
    ctx = {}
    ctx['successes'] = []
    ctx['warnings'] = []
    ctx['infos'] = []
    ctx['dangers'] = []
    ctx['top_menu'] = "Menu"
    ctx['side_menu'] = "Add_Menu"
    
    if request.method == 'POST':
        # dane z POST
        form = MenuForm(request.POST)
        if form.is_valid():
            print 'ok'
            form.save()
            # dane poprawne
            return HttpResponseRedirect('/menu/menu')
        else:
            print "not ok news"
            # dane niepoprawne
            pass
    else:
        # formularz
        form = MenuForm()
    
    ctx['form'] = form
    return render_to_response('menu/add_menu.html',
            ctx,
            context_instance=RequestContext(request))

@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_menu(request, menu_index):
    ctx = {}
    ctx['successes'] = []
    ctx['warnings'] = []
    ctx['infos'] = []
    ctx['dangers'] = []
    ctx['menus'] = Menu.objects.all()
    ctx['top_menu'] = "Menu"
    ctx['side_menu'] = "Edit_Menu"
    ctx['id'] = menu_index
    
    menu_record = Menu.objects.get(id=menu_index)
    if request.method == "POST":
        form_save = MenuForm(request.POST, instance=menu_record)
        if form_save.is_valid():
            form_save.save()
            print "ok"
        else:
            print "not ok"
    else:
        pass
    ctx['form'] = MenuForm(instance=menu_record)
    
    return render_to_response('menu/edit_menu.html',
            ctx,
            context_instance=RequestContext(request))

@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_menu(request, menu_index):
    ctx = {}
    ctx['successes'] = []
    ctx['warnings'] = []
    ctx['infos'] = []
    ctx['dangers'] = []
    ctx['menus'] = Menu.objects.all().order_by('id')
    ctx['top_menu'] = "Menu"
    ctx['side_menu'] = "Delete_Menu"
    
    Menu.objects.filter(id=menu_index).delete()
    #print "index: ", news_index
    print "len:", len(ctx['menus']), menu_index
    
    return render_to_response('menu/menu.html',
            ctx,
            context_instance=RequestContext(request))
    
@login_required
@user_passes_test(lambda u: u.is_superuser)
def dishes(request):
    ctx = {}
    ctx['successes'] = []
    ctx['warnings'] = []
    ctx['infos'] = []
    ctx['dangers'] = []
    ctx['top_menu'] = "Menu"
    ctx['side_menu'] = "Dishes"
    ctx['dishes'] = Dish.objects.all()
    
    paginator = Paginator(ctx['dishes'], 5) # Show 5 dishes per page

    page = request.GET.get('page')
#     print "p.count: ", page.count
#     print "p.num_pages: ", page.num_pages
#     print "p.page_range: ", page.page_range
    try:
        ctx['dishes_pags'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        ctx['dishes_pags'] = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        ctx['dishes_pags'] = paginator.page(paginator.num_pages)
    
    return render_to_response('menu/dishes.html',
            ctx,
            context_instance=RequestContext(request))

@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_dish(request):
    ctx = {}
    ctx['successes'] = []
    ctx['warnings'] = []
    ctx['infos'] = []
    ctx['dangers'] = []
    ctx['top_menu'] = "Menu"
    ctx['side_menu'] = "Add_Dish"
    
    if request.method == 'POST':
        # dane z POST
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            print 'ok valid dish'
            form.save()
            # dane poprawne
            return HttpResponseRedirect('/menu/dishes')
        else:
            print "not ok news invalid dish"
            # dane niepoprawne
            pass
    else:
        # formularz
        form = DishForm()
    
    ctx['form'] = form
    
    return render_to_response('menu/add_dish.html',
            ctx,
            context_instance=RequestContext(request))

@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_dish(request, dish_index):
    ctx = {}
    ctx['successes'] = []
    ctx['warnings'] = []
    ctx['infos'] = []
    ctx['dangers'] = []
    ctx['top_menu'] = "Menu"
    ctx['side_menu'] = "Edit_Dish"
    ctx['id'] = dish_index
    
    dish_record = Dish.objects.get(id=dish_index)
    if request.method == "POST":
        form_save = DishForm(request.POST, instance=dish_record)
        if form_save.is_valid():
            form_save.save()
            print "ok"
        else:
            print "not ok"
    else:
        form_save = DishForm(instance=dish_record)
        
    ctx['form'] = form_save
    
    return render_to_response('menu/edit_dish.html',
            ctx,
            context_instance=RequestContext(request))

@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_dish(request, dish_index):
    ctx = {}
    ctx['successes'] = []
    ctx['warnings'] = []
    ctx['infos'] = []
    ctx['dangers'] = []
    ctx['dishes'] = Dish.objects.all()
    ctx['top_menu'] = "Menu"
    ctx['side_menu'] = "Delete_Dish"
    
    Dish.objects.filter(id=dish_index).delete()
    #print "index: ", news_index
    print "len:", len(ctx['dishes']), dish_index
    
    return render_to_response('menu/dishes.html',
            ctx,
            context_instance=RequestContext(request))

@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_error(request, error_index):
    ctx = {}
    ctx['successes'] = []
    ctx['warnings'] = []
    ctx['infos'] = []
    ctx['dangers'] = []
    ctx['top_menu'] = "Menu"
    ctx['side_menu'] = "Clients_Errors"
    ctx['errors'] = Error.objects.all()
    
    Error.objects.filter(id=error_index).delete()
    #print "index: ", news_index
    print "len:", len(ctx['errors']), error_index
    
    return render_to_response('menu/clients_errors.html',
            ctx,
            context_instance=RequestContext(request))

@login_required
@user_passes_test(lambda u: u.is_superuser)
def clients_errors(request):
    ctx = {}
    ctx['successes'] = []
    ctx['warnings'] = []
    ctx['infos'] = []
    ctx['dangers'] = []
    ctx['top_menu'] = "Menu"
    ctx['side_menu'] = "Clients_Errors"
    ctx['errors'] = Error.objects.all()
    
    return render_to_response('menu/clients_errors.html',
            ctx,
            context_instance=RequestContext(request))

if __name__ == '__main__':
    pass