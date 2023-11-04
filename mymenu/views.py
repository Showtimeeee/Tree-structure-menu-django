from django.shortcuts import render
from mymenu.models import MenuItem
from django.http import HttpResponse


def draw_menu(request, menu_name):
    menu_items = MenuItem.objects.filter(name=menu_name).select_related('parent')
    return render(request, 'mymenu/menu.html', {'menu_items': menu_items})


def index(request):
    return HttpResponse('Пройдите по ссылке: <h1><a href="/mainmenu/">http://127.0.0.1:8000/mainmenu/</a></h1>')


def post_detail(request, name):
    names = MenuItem.objects.values_list('name', flat=True)
    return render(request, 'mymenu/detail.html', {'menu_item': names, 'name': name})