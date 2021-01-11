from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
from .views import (
    ContractViewSet,
    ContractDetailViewSet,
    CurrencyViewSet,
    ExchangeRateViewSet, MeasuringUnitViewSet, ItemTypeViewSet, VATViewSet, ItemViewSet    
)
router = routers.DefaultRouter(trailing_slash=False)
router.register('contracts', ContractViewSet, basename='contracts')
router.register('contract-detail', ContractDetailViewSet, basename='contract-detail')
router.register('currency', CurrencyViewSet, basename='currency')
router.register('exchange-rate', ExchangeRateViewSet, basename='exchange-rate')
router.register('measuring-unit', MeasuringUnitViewSet, basename='measuring-unit')
router.register('item-type', ItemTypeViewSet, basename='item-type')
router.register('vat', VATViewSet, basename='vat')
router.register('item', ItemViewSet, basename='item')

urlpatterns = router.urls

urlpatterns += [
    path('api-token/', TokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),
    path('contracts', ContractViewSet),    
    path('contract-detail', ContractDetailViewSet),  
    path('currency', CurrencyViewSet),  
    path('exchange-rate', ExchangeRateViewSet),  
    path('measuring-unit', MeasuringUnitViewSet),  
    path('item-type', ItemTypeViewSet),  
    path('vat', VATViewSet),
    path('item', ItemViewSet),
]