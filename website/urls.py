from django.conf.urls import url
from website import views
from django.views.generic import TemplateView


urlpatterns = [
    url(
        r'robots.txt$',
        TemplateView.as_view(
            template_name="website/robots.txt",
            content_type="text/plain"
        ), name="robots_file"
    ),
    url(
        r'humans.txt$',
        TemplateView.as_view(
            template_name="website/humans.txt",
            content_type="text/plain"
        ), name="humans_file"
    ),
    url(r'^diabetes/', views.diabetes, name='diabetes'),
    url(r'^diet-and-exercise/', views.diet_and_exercise, name='diet_and_exercise'),
    url(r'^plans/', views.plans, name='plans'),

    url(r'^faq/', views.faq, name='faq'),
    url(r'^cookies/', views.cookies, name='cookies'),
    url(r'^terms-and-conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    url(r'^$', views.home, name='home'),
]


