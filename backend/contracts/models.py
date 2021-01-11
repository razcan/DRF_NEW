from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify


User = get_user_model()

class Currency(models.Model):
    name = models.CharField(max_length=256, verbose_name="name")
    code = models.CharField(max_length=256, verbose_name="code")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)   

class ExchangeRate(models.Model):
    currency_id = models.ForeignKey(Currency, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, verbose_name="name")
    value = models.FloatField()
    at_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)        

    def __str__(self):
        return str(self.name)   


class Contract(models.Model):
    number = models.CharField(max_length=256, verbose_name="number")
    code = models.CharField(max_length=256, verbose_name="code")
    start_date = models.DateField()
    end_date = models.DateField()
    approved_date = models.DateField()
    currency_id = models.ForeignKey(Currency, on_delete=models.CASCADE)
    partner_id = models.IntegerField()
    partner_address_id = models.IntegerField()   
    notes = models.TextField(null=True)
    dimm_1 = models.IntegerField(blank=True, null=True)
    dimm_2 = models.IntegerField(blank=True, null=True)
    dimm_3 = models.IntegerField(blank=True, null=True)
    dimm_4 = models.IntegerField(blank=True, null=True)
    category_id = models.IntegerField(null=True)
    self_partner_id = models.IntegerField()
    status_id = models.IntegerField(default=1)
    responsible_id = models.IntegerField()
    repartization_key = models.TextField()
    renewel_type_id = models.IntegerField()
    renewel_end_date = models.DateTimeField()
    penalty_percent_day = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    attachment = models.FileField(blank=True, null=True, default='')

    def __str__(self):
        return f'{self.number} {self.start_date} {self.code}'

class MeasuringUnit(models.Model):
    name = models.CharField(max_length=256, verbose_name="name")
    code = models.CharField(max_length=256, verbose_name="code")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)   

class ItemType(models.Model):
    name = models.CharField(max_length=256, verbose_name="name")
    code = models.CharField(max_length=256, verbose_name="code")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)   

class VAT(models.Model):
    name = models.CharField(max_length=256, verbose_name="nmae")
    code = models.CharField(max_length=256, verbose_name="code")
    percent = models.IntegerField(verbose_name="percent")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)    
    
class Item(models.Model):
    name = models.CharField(max_length=256, verbose_name="name")
    measuring_unit_id = models.ForeignKey(MeasuringUnit, on_delete=models.CASCADE)
    item_type_id = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    vat_id = models.ForeignKey(VAT, on_delete=models.CASCADE)
    code = models.CharField(max_length=256, verbose_name="code")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)    

class ContractDetail(models.Model):    
    contract_id = models.ForeignKey(Contract, related_name='ctr_details', on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, related_name='items', on_delete=models.CASCADE)
    qtty = models.DecimalField(max_digits=10,default=0,decimal_places=2)
    price = models.DecimalField(max_digits=10,default=0,decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    value = models.DecimalField(max_digits=10,default=0,decimal_places=2)


    def save(self, *args, **kwargs):
        self.value = self.qtty * self.price        
        super(ContractDetail, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id) +""+ str(self.contract_id) +""+ str(self.item_id)
        # ,self.qtty,self.price,self.user)    