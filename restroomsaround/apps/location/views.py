from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.gis import geos, measure

from apps.location.models import LocationModel
from apps.location.forms import LocationForm

class HomePageView(generic.ListView):

	template_name = 'location/index.html'

	def get(self, request, *args, **kwargs):
		formObj = LocationForm(request.GET)
		return render(request, self.template_name, {
				'form': formObj,
			})


class LocationView(generic.ListView):

	template_name = 'location/nearby.html'

	def get(self, request, *args, **kwargs):
		formObj = LocationForm(request.GET)
		near_by_point = None
		if formObj.is_valid():
			lat = formObj.cleaned_data['lat']
			lng = formObj.cleaned_data['lng']
			default_distance = 10
			distance_from_point = {'km':default_distance}
			if lat and lng:
				current_point=geos.fromstr("POINT(%s %s)" % (lng, lat))
				near_by_point = LocationModel.objects.filter(
					location__distance_lte=(
						current_point,measure.D(**distance_from_point)))
				near_by_point = near_by_point.distance(current_point).order_by(
					'distance')

		html = render_to_string(self.template_name, {'restrooms': near_by_point})
		return JsonResponse({
				'points': html
			})


class SaveLocation(generic.CreateView):

	def post(self, request, *args, **kwargs):
		formObj = LocationForm(request.POST)
		info_msg, bstrp_cls = [None]*2
		d = {}
		if formObj.is_valid():
			lat = formObj.cleaned_data.get('lat', None)
			lng = formObj.cleaned_data.get('lng', None)
			if lat and lng:
				point = "POINT({} {})".format(lng, lat)
				point = geos.fromstr(point)
				pointExist = LocationModel.objects.filter(location__distance_lte=(point,measure.D(mi=0.001))).distance(point)
				if not pointExist:
					new_point = formObj.save(commit=False)
					new_point.location = point
					new_point.save()
					info_msg = "Your location is successfully saved"
					bstrp_cls = 'alert-success'
				else:
					info_msg = 'This location already exists in our database.'
					bstrp_cls = 'alert-warning'
		d['msg'] = info_msg
		d['cls'] = bstrp_cls
		return JsonResponse(d)
