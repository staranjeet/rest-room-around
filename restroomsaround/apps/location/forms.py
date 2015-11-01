from django.forms import ModelForm, TextInput
from apps.location.models import LocationModel

class LocationForm(ModelForm):

	class Meta:
		model = LocationModel
		fields = ['address', 'lat', 'lng']
		widgets = {
			'address': TextInput(attrs={'class': 'form-control', 'placeholder': 'Current address'}),
			'lat': TextInput(attrs={'class': 'form-control', 'placeholder': 'Latitude'}),
			'lng': TextInput(attrs={'class': 'form-control', 'placeholder': 'Longitude'})
		}
