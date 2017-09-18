from django.db import models
from django.conf import settings

from hours.models import HoursLocation

class Task(models.Model):
	owner				= models.ForeignKey(settings.AUTH_USER_MODEL)
	locations			= models.ForeignKey(HoursLocation)

	taskname   			= models.CharField(max_length =120)
	taskdetail         	= models.TextField (blank=True, null=True)
	public				= models.BooleanField(default =True)
	timestamp    		= models.DateTimeField(auto_now_add =True)
	updated	     		= models.DateTimeField(auto_now=True)

	class Meta:
		ordering= ('-timestamp', '-updated')
