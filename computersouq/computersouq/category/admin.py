from django.contrib import admin
from .models import Laptops, ram, hard
@admin.register(Laptops)
class LaptopsAdmin(admin.ModelAdmin):
    list_display= ['id' ,'Brand', 'Model', 'Quantity', 'Avilable_on_stock', 'Avilable_on_store']
    list_display_links= ['id', 'Brand', 'Model']
    search_fields= ['Model', 'Brand', 'id']
    list_filter= ['DateTime', 'Brand'] 
    list_editable= ['Quantity', 'Avilable_on_stock', 'Avilable_on_store']

@admin.register(ram)
class ram_admin(admin.ModelAdmin):
    list_display= ['Brand' ,'Type','Condition', 'Size', 'Speed', 'Price', 'Quantity', 'Available']
    list_editable = ['Available', 'Quantity']
    
@admin.register(hard)
class hard_admin(admin.ModelAdmin):
    list_display= ['Brand' ,'Type', 'Condition', 'Size', 'Price', 'Quantity', 'Available']
    list_editable = ['Available', 'Quantity']