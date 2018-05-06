from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.template import loader


def home(request):
    return render(request, template_name='website/home.html')


def view404(request):
    return HttpResponseNotFound(request, template_name='website/404.html')


"""
Custom error pages
"""


def custom_404_view(request, exception=None, template_name='website/404.html'):
    template = loader.get_template(template_name)
    return HttpResponseNotFound(template.render({}, request))


def custom_500_view(request, exception=None, template_name='website/500.html'):
    template = loader.get_template(template_name)
    return HttpResponseServerError(template.render({}, request))
