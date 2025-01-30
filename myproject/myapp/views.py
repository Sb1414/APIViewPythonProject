from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Attraction
from .serializers import AttractionSerializer


class AttractionAPIView(APIView):
    def get(self, request, *args, **kwargs):
        attractions = Attraction.objects.all()
        serializer = AttractionSerializer(attractions, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = AttractionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        attraction_id = kwargs.get('id')
        try:
            attraction = Attraction.objects.get(id=attraction_id)
            attraction.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Attraction.DoesNotExist:
            return Response({"Ошибка": "Аттракцион не найден"}, status=status.HTTP_404_NOT_FOUND)

    def encode(self, data):
        # Example encode method
        return data.encode('utf-8')

    def decode(self, data):
        # Example decode method
        return data.decode('utf-8')
