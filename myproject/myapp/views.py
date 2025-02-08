from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Attraction
from .serializers import AttractionSerializer

class AttractionAPIList(generics.ListCreateAPIView):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer


class AttractionAPIUpdate(generics.UpdateAPIView):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer


class AttractionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer


# class AttractionAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         attractions = Attraction.objects.all()
#         serializer = AttractionSerializer(attractions, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, *args, **kwargs):
#         serializer = AttractionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"Ошибка": "ID не указан, удаление невозможно"}, status=status.HTTP_400_BAD_REQUEST)
#
#         try:
#             attraction = Attraction.objects.get(pk=pk)
#             attraction.delete()
#             return Response({"Успех": f"Аттракцион {pk} удалён"}, status=status.HTTP_204_NO_CONTENT)
#         except Attraction.DoesNotExist:
#             return Response({"Ошибка": "объект не существует"}, status=status.HTTP_404_NOT_FOUND)
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"Ошибочка": "put невозможен"})
#
#         try:
#             instance = Attraction.objects.get(pk=pk)
#         except:
#             return Response({"Ошибочка": "объект не существует"})
#
#         serializer = AttractionSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"Post": serializer.data})


