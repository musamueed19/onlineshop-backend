from rest_framework import generics
from .models import Category, Product, Order
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer

# --- PRODUCT VIEWS ---
# 1. To Create and List Products only, Just do, ListCreateAPIView
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# 2. To do ALL CRUD, List - do RetrieveUpdateDestroyAPIView
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# --- CATEGORY VIEWS ---
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# --- ORDER VIEWS ---
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
