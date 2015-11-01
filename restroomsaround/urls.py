from django.conf.urls import include, url
from django.contrib import admin

from apps.location.views import HomePageView

urlpatterns = [

    url(r'^$', HomePageView.as_view(), name='home_page'),

    url(r'^location/',
        include('apps.location.urls', namespace="location")),

    url(r'^admin/', include(admin.site.urls)),
]
