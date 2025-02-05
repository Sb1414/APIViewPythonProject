from typing import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Category, Attraction

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class AttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attraction
        fields = '__all__'

    def create(self, validated_data):
        return Attraction.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.price = validated_data.get("price", instance.price)
        instance.category = validated_data.get("category", instance.category)
        instance.created_at = validated_data.get("created_at", instance.created_at)
        instance.save()
        return instance


def encode():
    model = Attraction('первый', 'описание', '600', '1')
    model_sr = AttractionSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json)


def decode():
    stream = io.BytesIO(b'{"name":"Первый","description":"lolololo", "price":600, "category":1, }')
    data = JSONParser().parse(stream)
    serializer = AttractionSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)