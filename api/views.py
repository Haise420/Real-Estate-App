from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.http import JsonResponse
from backend.models import *
from .serializers import PropertySerializer


@api_view(['GET'])
def getProperties(request):

    properties = Property.objects.all()

    serializer = PropertySerializer(properties, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getProperty(request, note_id):

    property = Property.objects.get(id=note_id)

    serializer = PropertySerializer(property, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def createProperty(request):
    serializer = PropertySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteProperty(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    property.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
