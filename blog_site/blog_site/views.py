from django.views.generic import TemplateView
from django.shortcuts import render
from django.apps import apps


class IndexView(TemplateView):
    http_method_names = ['get']
    template_name = "index.html"


class AboutView(TemplateView):
    http_method_names = ['get']
    template_name = "about.html"


class ContactView(TemplateView):
    http_method_names = ['get']
    template_name = "contact.html"


class PostView(TemplateView):
    http_method_names = ['get']
    template_name = "post.html"
