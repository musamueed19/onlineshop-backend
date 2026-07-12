from django.contrib import admin
from .models import Product, Category, Order


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Shows these columns in admin dashboard List
    list_display = ('id', 'category_name', 'description', 'created_at', 'updated_at')
    exclude = ('deleted_at',)
    
    # provide search filters
    search_fields = ('category_name', 'description')
    
    # provide filter options
    list_filter = ('created_at', 'updated_at', 'deleted_at')
  
@admin.register(Product)  
class ProductAdmin(admin.ModelAdmin):
    # Shows these columns in admin dashboard List
    list_display = ('id', 'product_name', 'description','category','price',  'created_at', 'updated_at')
    exclude = ('deleted_at',)
    
    # provide search filters
    search_fields = ('product_name', 'description', 'price', 'category__category_name')
    
    # provide filter options
    list_filter = ('category__category_name','price','created_at', 'updated_at', 'deleted_at')
  

@admin.register(Order)  
class OrderAdmin(admin.ModelAdmin):
    # Shows these columns in admin dashboard List
    list_display = ('id', 'customer_name', 'customer_email','product','quantity',  'created_at', 'updated_at')
    exclude = ('deleted_at',)
    
    # provide search filters
    search_fields = ('customer_name', 'customer_email', 'product__product_name')
    # provide filter options
    list_filter = ('product__product_name','customer_email','created_at', 'updated_at', 'deleted_at')