from django.shortcuts import render
from django.views.generic.base import TemplateView 

# Create your views here.
class mainView(TemplateView):
    template_name="core/index.html"
