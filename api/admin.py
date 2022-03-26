from django.contrib import admin
from .models import(Product, Discount, Amount)
# # Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ["name",]
    search_fields = ("name",)
    list_filter = ('create_at',)
    ordering = ('id',)

    # fields = (
    #     'name', 'price_num_1'
    # )
    
@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['product',]
    search_fields = ('product',)
    list_filter = ('product', 'create_at',)
    ordering = ('id',)

    # fields = (
    #     'discount_10m',
    # )
@admin.register(Amount)
class AmountAdmin(admin.ModelAdmin):
    list_display = ('get_products', 'name', 'price_of')
    list_filter = ('product', 'create_at',)
    search_fields = ('name',)
    ordering = ('id',)