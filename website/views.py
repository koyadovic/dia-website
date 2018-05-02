from django.shortcuts import render


def home(request):
    return render(request, template_name='website/home.html')


def view404(request):
    return render(request, template_name='website/404.html')
