from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.template import loader


"""
Pages
"""


def home(request):
    return render(request, template_name='website/home.html')


def diet_and_exercise(request):
    return render(request, template_name='website/diet_and_exercise.html')


def diabetes(request):
    return render(request, template_name='website/diabetes.html')


def plans(request):
    return render(request, template_name='website/plans.html')


def faq(request):
    return render(request, template_name='website/faq.html')


def cookies(request):
    return render(request, template_name='website/cookies.html')


def terms_and_conditions(request):
    return render(request, template_name='website/terms_and_conditions.html')


"""
Custom error pages
"""


def custom_404_view(request, exception=None, template_name='website/404.html'):
    template = loader.get_template(template_name)
    return HttpResponseNotFound(template.render({}, request))


def custom_500_view(request, exception=None, template_name='website/500.html'):
    template = loader.get_template(template_name)
    return HttpResponseServerError(template.render({}, request))
