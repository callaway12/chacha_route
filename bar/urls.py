from django.contrib import admin
from django.urls import path, include
import bar.views

urlpatterns = [
    path('', bar.views.home, name='home'),
    path('select', bar.views.select, name='select'),
    path('done_select', bar.views.done_select, name='done_select'),
]
