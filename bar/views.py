from django.shortcuts import render, redirect
from bar.models import Product
from user.models import User, Route
from datetime import datetime
from django.utils import formats
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format

# Create your views here.
def home(request):
    products = Product.objects.all()
    current_user_id = request.user.id


    return render(request, 'home.html', {'pros':products, 'current_user_id':current_user_id})



def select(request):
    if not request.user.first:
        dt = datetime.now()
        df = DateFormat(dt)
        df.format(get_format('DATE_FORMAT'))
        df.format('Y-m-d')
        tmp_first = request.POST['bar_id_name']
        obj = Product.objects.get(pk=tmp_first)
        current_user = request.user
        current_user.first = obj
        current_user.first_date = dt
        current_user.save()

    elif not request.user.second:
        tmp_second = request.POST['bar_id_name']
        obj = Product.objects.get(pk=tmp_second)
        current_user = request.user
        current_user.second = obj
        current_user.save()

    elif not request.user.third:
        tmp_third = request.POST['bar_id_name']
        obj = Product.objects.get(pk=tmp_third)
        current_user = request.user
        current_user.third = obj
        current_user.save()
    
    return redirect('home')


    
def done_select(request):
    route = Route()
    current_user = request.user
    route.author = current_user
    route.pub_date = current_user.first_date
    route.first_bar = current_user.first
    if current_user.second:
        route.second_bar = current_user.second
    elif current_user.thire:
        route.third_bar = current_user.third

    route.save()

    current_user.first = None
    current_user.second = None
    current_user.third = None

    current_user.save()

    return redirect('home')