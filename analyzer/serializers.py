from rest_framework import serializers
from .models import OptionChainSnapshot

class OptionChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionChainSnapshot
        fields = '__all__'