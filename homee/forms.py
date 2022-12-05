
from django.forms import ModelForm
from .models import detail

class createform(ModelForm):
	class Meta:
		model = detail
		fields = '__all__'
		