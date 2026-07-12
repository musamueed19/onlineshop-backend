from django.urls import path
from .views import (
    OrderView
)

urlpatterns = [
    # Orders Endpoint: /api/orders/
    path('order/', OrderView.as_view(), name='order'),
]
