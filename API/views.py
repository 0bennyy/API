from django.shortcuts import render
from django.http import JsonResponse
from .models import product
from .serializers import productSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def product_list(request, format=None):
    if request.method == 'GET':
        products = product.objects.all()
        serializer = productSerializer(products, many=True)  # Renamed from 'productSerializer'
        return Response(serializer.data)
