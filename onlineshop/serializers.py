from rest_framework import serializers
from .models import Category, Product, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'description']

class ProductSerializer(serializers.ModelSerializer):
    # Category ki poori detail dekhne ke liye (Optional)
    category_detail = CategorySerializer(source='category', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'description', 'price', 'category', 'category_detail']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer_name', 'customer_email', 'quantity', 'product', 'created_at']
