from django import forms
from .models import HoursLocation

class DateInput(forms.DateInput):
    input_type = 'date'

class HoursCreateForm(forms.Form):
	OpportunityNumber   = forms.CharField(required=False)
	ChildsName         	= forms.CharField(required=False)
	location     		= forms.CharField(required=False)
	hours        		= forms.CharField(required=False)
	my_date_field		= forms.DateField(required=False)

class HoursLocationCreateForm(forms.ModelForm):
	class Meta: 
		model = HoursLocation
		fields =[
				'OpportunityNumber',
				'ChildsName',
				'location',
				'my_date_field',
				'hours',
				# 'owner'

		]
