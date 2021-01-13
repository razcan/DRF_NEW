from django.shortcuts import render
from django.db.models import Count
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import SAFE_METHODS, AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters
# from django_filters.rest_framework import DjangoFilterBackend



from .serializers import (
    ContractSerializer, CurrencySerializer , ExchangeRateSerializer, MeasuringUnitSerializer, 
    ItemTypeSerializer, VATSerializer, ItemSerializer, ContractDetailSerializer,PartnerSerializer,StateSerializer
)
from .models import Contract, Currency , ExchangeRate, MeasuringUnit, ItemType, VAT, Item, ContractDetail,Partner,State

class ContractViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)  
    ordering_fields = ['id']
    # queryset = Contract.objects.all()
    queryset = Contract.objects.raw("SELECT id FROM contracts_contract where id=2")
    serializer_class = ContractSerializer
    pagination_class = PageNumberPagination


class ContractDetailViewSet(viewsets.ModelViewSet):    
    #permission_classes = (IsAuthenticated,)  
    ordering_fields = ['id']
    queryset = ContractDetail.objects.all()
    serializer_class = ContractDetailSerializer
    pagination_class = PageNumberPagination

class CurrencyViewSet(viewsets.ModelViewSet):    
    #permission_classes = (IsAuthenticated,)  
    ordering_fields = ['id']
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = PageNumberPagination

class ExchangeRateViewSet(viewsets.ModelViewSet):    
    #permission_classes = (IsAuthenticated,)  
    ordering_fields = ['id']
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRateSerializer
    pagination_class = PageNumberPagination    

class MeasuringUnitViewSet(viewsets.ModelViewSet):    
    ##permission_classes = (IsAuthenticated,)  
    ordering_fields = ['id']
    queryset = MeasuringUnit.objects.all()
    serializer_class = MeasuringUnitSerializer
    pagination_class = PageNumberPagination     

class ItemTypeViewSet(viewsets.ModelViewSet):    
    #permission_classes = (IsAuthenticated,)  
    ordering_fields = ['id']
    queryset = ItemType.objects.all()
    serializer_class = ItemTypeSerializer
    pagination_class = PageNumberPagination     

class VATViewSet(viewsets.ModelViewSet):    
    #permission_classes = (IsAuthenticated,)  
    ordering_fields = ['id']
    queryset = VAT.objects.all()
    serializer_class = VATSerializer
    pagination_class = PageNumberPagination    

class ItemViewSet(viewsets.ModelViewSet):    
    #permission_classes = (IsAuthenticated,)  
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        user = self.request.user
        # tip = self.request.method
        # print(tip);
        # print(user);
        queryset = Item.objects.all()
        # url : http://127.0.0.1:8000/api/item?username=admin
        username = self.request.query_params.get('username', None)
        print(username);
        if (username == 'admin'):
            user_id = 1
        else: 
            user_id = 2
        queryset = queryset.filter(user=user_id)
        return queryset          

class StateViewSet(viewsets.ModelViewSet):    
    #permission_classes = (IsAuthenticated,)  
    ordering_fields = ['id']
    queryset = State.objects.all()

class PartnerViewSet(viewsets.ModelViewSet):    
    #permission_classes = (IsAuthenticated,)  
    ordering_fields = ['id']
    queryset = Partner.objects.all()    