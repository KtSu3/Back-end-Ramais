from rest_framework import viewsets
from .serializers import RamaisSerializer
from .models import Ramais
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

class RamaisViewSet(viewsets.ModelViewSet):
    queryset = Ramais.objects.all()
    serializer_class = RamaisSerializer



        
