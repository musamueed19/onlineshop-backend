from rest_framework import serializers
from .models import Category, Product, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__' # All fields of the Category model
        # depth = 1

class ProductSerializer(serializers.ModelSerializer):
    # To get complete detail of category, based on a reference_key category in product record
    # category_detail = CategorySerializer(source='category', read_only=True)

    class Meta:
        model = Product
        fields = '__all__' # All fields of the Product model
        depth = 2

class OrderSerializer(serializers.ModelSerializer):
    # depth makes FK fields read-only; keep nested product on read, accept ID on write
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source="product",
        write_only=True,
    )

    class Meta:
        model = Order
        fields = "__all__"
