from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.models import Group, User


# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

class Redirecionamento(TemplateView):
    template_name = "redirecionamentoLogin.html"
    
