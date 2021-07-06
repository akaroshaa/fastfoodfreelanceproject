from django.contrib import admin
from .models import FoodItem

# Register your models here.
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description", "price", "picture"]


admin.site.register(FoodItem, FoodItemAdmin)
