from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from django.conf import settings
from django.core.urlresolvers import reverse


# Create your models here.
User = settings.AUTH_USER_MODEL

class HoursLocation(models.Model):
	owner				= models.ForeignKey(User)
	OpportunityNumber   = models.CharField(max_length =120)
	ChildsName         	= models.CharField(max_length =120)
	location     		= models.CharField(max_length =120, null=True, blank =True)
	hours        		= models.CharField(max_length =120, null = True, blank = True)
	timestamp    		= models.DateTimeField(auto_now_add =True)
	updated	     		= models.DateTimeField(auto_now=True)
	my_date_field		= models.DateField(auto_now=False, auto_now_add=False)
	slug  				= models.SlugField(null=True, blank =True)

	def __str__(self):
		return self.OpportunityNumber

	def get_absolute_url(self):
		return reverse('hours:detail',kwargs={'slug': self.slug})


	@property
	def title(self):
		return self.OpportunityNumber


def hl_pre_save_receiver(sender, instance,*args,**kwargs):
	print('saving..')
	print(instance.timestamp)
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

def hl_post_save_receiver(sender, instance,created, *args,**kwargs):
	print('saved..')
	print(instance.timestamp)

pre_save.connect(hl_pre_save_receiver, sender=HoursLocation)
post_save.connect(hl_post_save_receiver, sender=HoursLocation)