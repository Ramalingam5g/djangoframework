from rest_framework import serializers
from . models import material

class material_list(serializers.Modelserializers):
    class Meta:
        model = material
        fields ='__all__'