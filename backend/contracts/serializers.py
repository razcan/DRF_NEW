from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Contract, Currency , ExchangeRate, MeasuringUnit, ItemType, VAT, Item, ContractDetail

User = get_user_model()

class ContractSerializer(serializers.ModelSerializer):
    # number = serializers.CharField()
    # code = serializers.CharField()
    # start_date = serializers.DateField()
    # end_date = serializers.DateField()
    # approved_date = serializers.DateField()
    # currency_id = serializers.IntegerField()
    # partner_id = serializers.IntegerField()
    # partner_address_id = serializers.IntegerField()   
    # notes = serializers.CharField()
    # dimm_1 = serializers.IntegerField()
    # dimm_2 = serializers.IntegerField()
    # dimm_3 = serializers.IntegerField()
    # dimm_4 = serializers.IntegerField()
    # category_id = serializers.IntegerField()
    # self_partner_id = serializers.IntegerField()
    # status_id = serializers.IntegerField()
    # responsible_id = serializers.IntegerField()
    # repartization_key = serializers.CharField()
    # renewel_type_id = serializers.IntegerField()
    # renewel_end_date = serializers.DateTimeField()
    # penalty_percent_day = serializers.IntegerField()
    # created = serializers.DateTimeField()
    # updated = serializers.DateTimeField()
    # attachment = serializers.FileField()   
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Contract
        fields = '__all__'

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'

class ExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = '__all__'

class MeasuringUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasuringUnit
        fields = '__all__'

class ItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemType
        fields = '__all__'

class VATSerializer(serializers.ModelSerializer):
    class Meta:
        model = VAT
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ContractDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractDetail
        fields = '__all__'

