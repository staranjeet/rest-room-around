from django.contrib import admin

from apps.location.models import LocationModel

@admin.register(LocationModel)
class LocationModelAdmin(admin.ModelAdmin):

	list_display = ['address', 'lat', 'lng']
	list_display_links = ['address']
