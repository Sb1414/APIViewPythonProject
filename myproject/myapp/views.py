from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Attraction
from .serializers import AttractionSerializer


# class AttractionAPIView(ListCreateAPIView):
#     queryset = Attraction.objects.all()
#     serializer_class = AttractionSerializer

class AttractionAPIList(generics.ListCreateAPIView):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer


class AttractionAPIUpdate(generics.UpdateAPIView):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer


class AttractionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer


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
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})
        return Response({"post": "delete post " + str(pk)})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Attraction.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = AttractionSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})


