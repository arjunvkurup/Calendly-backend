from rest_framework import generics
from .serializers import CalendlySerializer
from calendly.models import Calendly


class CalendlyViewSet(generics.ListCreateAPIView):
    queryset = Calendly.objects.all()
    serializer_class = CalendlySerializer


class DetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Calendly.objects.all()
    serializer_class = CalendlySerializer
