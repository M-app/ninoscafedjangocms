from django import forms
from .models import Nino

class NinoCreateForm(forms.ModelForm):
	class Meta:
		model = Nino
		fields = [
			'nombres',
			'apellidos',
			'etapa',
			'historia',
			'foto',
		]