from django.conf.urls import url
from surveys import views


urlpatterns = [
    url(r'^$', view=views.survey_view, name='surveys'),
]
