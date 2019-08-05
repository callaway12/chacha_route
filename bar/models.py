from django.db import models
import datetime

 


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='상품명')
    price = models.IntegerField(verbose_name='상품가격')
    description = models.TextField(verbose_name='상품설명')
    stock = models.IntegerField(verbose_name='재고', null=True, blank=True)
    register_date = models.DateField(default=datetime.date.today, name='등록날짜')

    
    
    def __str__(self):
        return self.name

