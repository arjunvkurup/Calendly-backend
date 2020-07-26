from rest_framework import serializers
from calendly.models import Calendly


class CalendlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendly
        fields = '__all__'