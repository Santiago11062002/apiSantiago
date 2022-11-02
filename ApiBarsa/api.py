from .models import Barsa
from rest_framework import viewsets, permissions
from .serializers import BarsaSerializer

class BarsaviewSet(viewsets.ModelViewSet):
    queryset = Barsa.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BarsaSerializer