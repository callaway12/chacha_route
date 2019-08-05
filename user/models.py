from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from bar.models import Product



class User(AbstractUser):
   
    name = models.CharField(max_length=140, blank=True) 
    

    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜', blank=True)
    
    first = models.ForeignKey(Product,on_delete=models.CASCADE, null=True,related_name='+', blank=True)
    second = models.ForeignKey(Product,on_delete=models.CASCADE, null=True,related_name='+', blank=True)
    third = models.ForeignKey(Product,on_delete=models.CASCADE, null=True,related_name='+', blank=True)

    first_date = models.DateField(null=True, blank=True)


class Route(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    name_route = models.CharField(max_length=55, blank=False)
    pub_date = models.DateField(null=True, blank=True)

    first_bar = models.ForeignKey(Product,on_delete=models.CASCADE, null=True,related_name='+', blank=True)
    second_bar = models.ForeignKey(Product,on_delete=models.CASCADE, null=True,related_name='+', blank=True)
    third_bar = models.ForeignKey(Product,on_delete=models.CASCADE, null=True,related_name='+', blank=True)

    def __str__(self):
        pd = str(self.pub_date)
        return pd


        