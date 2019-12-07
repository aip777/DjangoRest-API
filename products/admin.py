from django.contrib import admin

from .forms import ProductsForm
from .models import Products


class StatusAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'code',   '__str__', 'price', 'image']
    form = ProductsForm

admin.site.register(Products, StatusAdmin)