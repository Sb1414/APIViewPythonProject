from typing import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Attraction

class AttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attraction
        fields = '__all__'


def encode():
    model = Attraction('first', 'first op', '600', '1')
    model_sr = AttractionSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json)


def decode():
    stream = io.BytesIO(b'{"name":"first","description":"lolololo", "price":600, "category":1, }')
    data = JSONParser().parse(stream)
    serializer = AttractionSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)