from django.shortcuts import render
from django.db.models import Count
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import (
    ContractSerializer, CurrencySerializer , ExchangeRateSerializer, MeasuringUnitSerializer, ItemTypeSerializer, VATSerializer, ItemSerializer, ContractDetailSerializer
)
from .models import Contract, Currency , ExchangeRate, MeasuringUnit, ItemType, VAT, Item, ContractDetail

class ContractViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)  
    ordering_fields = ['id']
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    pagination_class = PageNumberPagination


class ContractDetailViewSet(viewsets.ModelViewSet):    
    permission_classes = (IsAuthenticated,)  
    ordering_fields = ['id']
    queryset = ContractDetail.objects.all()
    serializer_class = ContractDetailSerializer
    pagination_class = PageNumberPagination

class CurrencyViewSet(viewsets.ModelViewSet):    
    permission_classes = (IsAuthenticated,)  
    ordering_fields = ['id']
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = PageNumberPagination

class ExchangeRateViewSet(viewsets.ModelViewSet):    
    permission_classes = (IsAuthenticated,)  
    ordering_fields = ['id']
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRateSerializer
    pagination_class = PageNumberPagination    

class MeasuringUnitViewSet(viewsets.ModelViewSet):    
    permission_classes = (IsAuthenticated,)  
    ordering_fields = ['id']
    queryset = MeasuringUnit.objects.all()
    serializer_class = MeasuringUnitSerializer
    pagination_class = PageNumberPagination     

class ItemTypeViewSet(viewsets.ModelViewSet):    
    permission_classes = (IsAuthenticated,)  
    ordering_fields = ['id']
    queryset = ItemType.objects.all()
    serializer_class = ItemTypeSerializer
    pagination_class = PageNumberPagination     

class VATViewSet(viewsets.ModelViewSet):    
    permission_classes = (IsAuthenticated,)  
    ordering_fields = ['id']
    queryset = VAT.objects.all()
    serializer_class = VATSerializer
    pagination_class = PageNumberPagination    

class ItemViewSet(viewsets.ModelViewSet):    
    permission_classes = (IsAuthenticated,)  
    ordering_fields = ['id']
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = PageNumberPagination            
