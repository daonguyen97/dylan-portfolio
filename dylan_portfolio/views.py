from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


def index(request):
    return TemplateView.as_view(template_name='portfolio/index.html')(request)
