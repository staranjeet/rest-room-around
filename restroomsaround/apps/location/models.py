from django.contrib.gis.db import models

class TimeAuditModel(models.Model):

	created_at = models.DateTimeField(u'Created At', auto_now_add=True, null=True)
	updated_at = models.DateTimeField(u'Last Updated At', auto_now=True, null=True)

	class Meta:
		abstract = True


class LocationModel(TimeAuditModel):

	address = models.CharField(max_length=255, verbose_name="Location of the rest room", null=True, blank=True)
	lat = models.FloatField(u'Latitude', blank=True)
	lng = models.FloatField(u'Longitude', blank=True)
	location = models.PointField(blank=True, null=True, verbose_name='Longitude/Latitude', geography=True)
	objects = models.GeoManager()

	def __unicode__(self):
		return unicode(self.id)

	class Meta:
		db_table = 'restroom'
		verbose_name_plural = 'Rest Rooms Location'

