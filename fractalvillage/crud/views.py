from rest_framework import viewsets
#from django.shortcuts import render
from fractalvillage.crud.models import *
from fractalvillage.crud.serializers import *

# Create your views here.

class VillageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Village.objects.all()
    serializer_class = VillageSerializer

class VillageDocsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VillageDocs.objects.all().order_by('doc_serial_number')
    serializer_class = VillageDocsSerializer

class CampViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Camp.objects.all()
    serializer_class = CampSerializer
