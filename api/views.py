from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.http import JsonResponse
from backend.models import *
from .serializers import ApartmentSerializer, HouseSerializer, AgencieSerializer, InvestorSerializer, BankSerializer


@api_view(['GET'])
def getProperties(request):
    apartments = Apartment.objects.all()    

    
    apartment_serializer = ApartmentSerializer(apartments, many=True)
    house_serializer = HouseSerializer(houses, many=True)

    combined_data = apartment_serializer.data + house_serializer.data

    return Response(combined_data)


@api_view(['GET'])
def getAgencies(request):

    agencies = Agencie.objects.all()
    agencies_serializer = AgencieSerializer(agencies, many=True)

    return Response(agencies_serializer.data)


@api_view(['GET'])
def getInvestors(request):

    investors = Investor.objects.all()
    investors_serializer = InvestorSerializer(investors, many=True)

    return Response(investors_serializer.data)

@api_view(['GET'])
def getBanks(request):

    banks = Bank.objects.all()
    banks_serializer = BankSerializer(banks, many=True)

    return Response(banks_serializer.data)

@api_view(['GET'])
def getProperty(request, property_id):
    try:
        property = Apartment.objects.get(id=property_id)
        serializer = ApartmentSerializer(property)
    except Apartment.DoesNotExist:
        property = get_object_or_404(House, id=property_id)
        serializer = HouseSerializer(property)

    return Response(serializer.data)


@api_view(['POST'])
def createProperty(request):
    if 'variety' in request.data and request.data['variety'] == 'apartment':
        serializer = ApartmentSerializer(data=request.data)
    elif 'variety' in request.data and request.data['variety'] == 'house':
        serializer = HouseSerializer(data=request.data)
    else:
        return Response({"error": "Invalid property type"}, status=status.HTTP_400_BAD_REQUEST)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteProperty(request, property_id):
    try:
        property = Apartment.objects.get(id=property_id)
    except Apartment.DoesNotExist:
        property = get_object_or_404(House, id=property_id)
    
    property.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)