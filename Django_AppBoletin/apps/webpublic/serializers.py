from rest_framework.serializers import ModelSerializer

from apps.webadmin.models import BoletinModelo

class BoletinSerializer(ModelSerializer):
	class Meta:
		model = BoletinModelo
		fields = ('titulo','resumen','tipo')

