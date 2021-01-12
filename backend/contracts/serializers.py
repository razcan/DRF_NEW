from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Contract, Currency , ExchangeRate, MeasuringUnit, ItemType, VAT, Item, ContractDetail

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'date_joined',
            'last_login',
            'auth_token'
        ]

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
    #items = ContractDetailSerializer(many=True, read_only=True)
    measuring_unit_id = MeasuringUnitSerializer()
    item_type_id = ItemTypeSerializer()
    vat_id = VATSerializer()
    user = UserSerializer()
    # measures = MeasuringUnitSerializer(many=True, read_only=True)
    class Meta:
        model = Item
        fields = '__all__'    


class ContractDetailSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    #items = serializers.RelatedField(many=True)
    #items = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # ctr_items = serializers.StringRelatedField(many=True, read_only=True)
    # ctr_items = serializers.HyperlinkedIdentityField(view_name='item')
    # ctr_items = ItemSerializer(many=True, read_only=True)
    # item_id = ItemSerializer(many=True, read_only=True)    
    #items = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = ContractDetail
        fields = '__all__'



class ContractSerializer(serializers.ModelSerializer):
    # ctr_details = serializers.StringRelatedField(many=True)
    #ctr_details = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    ctr_details = ContractDetailSerializer(many=True, read_only=True)
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

