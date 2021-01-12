from django.contrib import admin
from .models import Contract,Currency , ExchangeRate, MeasuringUnit, ItemType, VAT, Item, ContractDetail

admin.site.register(Contract)
admin.site.register(ContractDetail)
admin.site.register(Currency)
admin.site.register(ExchangeRate) 
admin.site.register(MeasuringUnit)
admin.site.register(ItemType) 
admin.site.register(VAT) 
admin.site.register(Item) 

