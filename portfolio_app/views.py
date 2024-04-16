from django.shortcuts import render
from django.views.generic.base import TemplateView


class home_view(TemplateView):
    template_name = "index.html"
