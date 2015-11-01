from django.contrib import admin

from apps.location.models import LocationModel

@admin.register(LocationModel)
class LocationModelAdmin(admin.ModelAdmin):

	list_display = ['address', 'lat', 'lng', 'created_at']
	list_display_links = ['address']
	list_filter = ['created_at']
