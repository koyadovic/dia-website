
from django.conf.urls import url
from django.contrib import admin
from django.urls import include


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('website.urls'))
]


handler404 = 'website.views.custom_404_view'
handler500 = 'website.views.custom_500_view'
