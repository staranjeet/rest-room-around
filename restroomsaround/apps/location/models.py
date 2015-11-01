from django.contrib.gis.db import models

class LocationModel(models.Model):

	address = models.CharField(max_length=255, verbose_name="Location of the rest room", null=True, blank=True)
	lat = models.FloatField(blank=True)
	lng = models.FloatField(blank=True)
	location = models.PointField(blank=True, null=True, verbose_name='Longitude/Latitude', geography=True)
	objects = models.GeoManager()

	def __unicode__(self):
		return unicode(self.id)

	class Meta:
		db_table = 'restroom'
		verbose_name_plural = 'Rest Rooms Location'

