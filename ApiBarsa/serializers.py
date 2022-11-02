
from rest_framework import serializers
from .models import Barsa

class BarsaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barsa
        fields = ('id','referencia','descripcion','nombre_del_club','pais_club','ciudad_representada','edad','titulos','nombre_estadio','capacidad_estadio','presidente_club')
        read_only_field = ('nombre_del_club')