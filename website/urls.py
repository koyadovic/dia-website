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
    url(r'', views.home),
]
