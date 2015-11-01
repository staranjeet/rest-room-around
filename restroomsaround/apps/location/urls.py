from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from .views import LocationView, SaveLocation

urlpatterns = [

	url(r'^nearby/', LocationView.as_view(), name='nearby_locations'),
	url(r'^save/', csrf_exempt(SaveLocation.as_view()), name='save_location'),

]
