from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializers import WomenSerializer


class WomenAPIView(APIView):
    def get(self, request):
        w = Women.objects.all()
        return Response({'postssss': WomenSerializer(w, many=True).data})

    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Methid out is not allowed"})

        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})

        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method delete is not allowed"})







# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
