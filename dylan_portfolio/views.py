from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Page
from .models import NavbarItem

NAV_BAR_ITEMS = NavbarItem.objects.filter(status = True)

def index(request):
    page = Page.objects.get(title = 'index')
    return render(request, str(page), {'page':page, 'items':NAV_BAR_ITEMS})

def projects(request):
    page = Page.objects.get(title = 'projects')
    return render(request, str(page), {'page':page, 'items':NAV_BAR_ITEMS})
