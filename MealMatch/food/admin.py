from django.contrib import admin
from .models import FoodItem 

class FoodItemAdmin(admin.ModelAdmin):
    list_display = ( 'seller','Item_name', 'quantity', 'price','location','photo','created_at')  # Adjust based on your fields
    search_fields = ('Item_name', 'seller__username')
    list_filter = ('seller', 'created_at')



admin.site.register(FoodItem, FoodItemAdmin)
