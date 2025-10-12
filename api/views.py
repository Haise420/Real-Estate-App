from rest_framework import viewsets
from backend.models import Apartment, House, Agencie, Investor, Bank
from .serializers import ApartmentSerializer, HouseSerializer, AgencieSerializer, InvestorSerializer, BankSerializer

class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class AgencieViewSet(viewsets.ModelViewSet):
    queryset = Agencie.objects.all()
    serializer_class = AgencieSerializer

class InvestorViewSet(viewsets.ModelViewSet):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer

class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer