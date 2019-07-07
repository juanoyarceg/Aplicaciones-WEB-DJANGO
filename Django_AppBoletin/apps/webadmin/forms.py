from django import forms
from apps.webadmin.models import BoletinModelo

class BoletinForm(forms.ModelForm):
	class Meta:
		model = BoletinModelo

		fields = [
			'titulo',
			'resumen',
			'detalle',
			'fecha',
			'tipo',
		]

		labels = {
			'titulo': 'Título',
			'resumen': 'Resumen',
			'detalle': 'Detalle',
			'fecha': 'Fecha (Año-Mes-Día)',
			'tipo': 'Tipo',
		}

		widgets = {
			'titulo':forms.TextInput(attrs={'class':'form-control'}),
			'resumen':forms.TextInput(attrs={'class':'form-control'}),
			'detalle':forms.Textarea(attrs={'class':'form-control','rows':3}),
			'fecha':forms.DateInput(attrs={'class':'form-control'}),
			'tipo':forms.Select(attrs={'class':'form-control'}),
		}

