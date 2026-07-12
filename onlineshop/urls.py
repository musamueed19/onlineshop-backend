from django.urls import path
from .views import (
    ProductListCreateView, ProductDetailView,
    CategoryListCreateView, OrderListCreateView
)

urlpatterns = [
    # Categories Endpoint: /api/categories/
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    
    # Products Endpoints: /api/products/ aur /api/products/1/
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    
    # Orders Endpoint: /api/orders/
    path('orders/', OrderListCreateView.as_view(), name='order-list'),
]
