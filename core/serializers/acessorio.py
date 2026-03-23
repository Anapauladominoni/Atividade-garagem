from rest_framework.serializers import ModelSerializer
from core.models import acessorio

class AcessorioSerializer(ModelSerializer):
    class Meta:
        model = acessorio.Acessorio
        fields = '__all__'