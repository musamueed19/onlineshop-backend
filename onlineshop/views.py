from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Product, Order
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer
from time import timezone
from django.core.mail import send_mail
from backend.settings import EMAIL_HOST_USER

# --- PRODUCT VIEWS ---
# 1. To Create and List Products only, Just do, ListCreateAPIView


# --- ORDER VIEWS ---
class OrderView(APIView):
    def get(self, request):
        try:
            # get all orders
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
            # return serializer response
            return Response(
                {
                    "data": serializer.data,
                    "success": True,
                    "message": "Orders retrieved successfully",
                    # 'timestamp': timezone.now()
                },
                status=status.HTTP_200_OK,
            )
        except Exception as error:
            print("Error List orders View ===== ", error)
            return Response(
                {
                    "error": str(error),
                    "success": False,
                    "message": "Failed to retrieve orders",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        # create

    def post(self, request):
        try:
            serializer = OrderSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()

                # send mail
                product_name = serializer.data.get("product", {}).get("product_name", "Product")
                subject = f"New {product_name} Order #{serializer.data.get('id')} is placed"
                message = f"""
Dear {serializer.data.get('customer_name')},
Thank you for placing an order at onlineshop.com.
Your order has been placed successfully and will be delivered soon.

Order Details:
Your Email: {serializer.data.get('customer_email')}

Order ID: {serializer.data.get('id')}
Product: {product_name}
Quantity: {serializer.data.get('quantity')}

Regards,
Online Shop Team
"""
                recipient_list = [request.data.get("customer_email"), "ahsannawab6@gmail.com"]

                # send mail to the customer
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=EMAIL_HOST_USER,
                    recipient_list=recipient_list,
                    fail_silently=False,
                )

                return Response(
                    {
                        "data": serializer.data,
                        "success": True,
                        "message": "Order created successfully",
                    },
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {
                        "error": serializer.errors,
                        "success": False,
                        "message": "Failed to create order",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as error:
            print("Error Create Order View ===== ", error)
            return Response(
                {
                    "error": str(error),
                    "success": False,
                    "message": "Failed to create order",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def patch(self, request):
        try:
            # get request data
            data = request.data
            order = Order.objects.filter(id=data.get("id"))

            # check if order, exists
            if not order.exists():
                return Response(
                    {
                        "success": False,
                        "message": f'Order with {data.get("id")} not found',
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            serializer = OrderSerializer(order[0], data=data, partial=True)
            if not serializer.is_valid():
                return Response(
                    {
                        "error": serializer.errors,
                        "success": False,
                        "message": f"Failed to update order {data.get('id')}",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            serializer.save()
            return Response(
                {
                    "data": serializer.data,
                    "success": True,
                    "message": f"Order {data.get('id')} updated successfully",
                },
                status=status.HTTP_200_OK,
            )
        except Exception as error:
            print("Error Update Order View ===== ", error)
            return Response(
                {
                    "error": str(error),
                    "success": False,
                    "message": f"Failed to update order {data.get('id')}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request):
        try:
            # get data from request
            data = request.data
            order = Order.objects.filter(id=data.get("id"))
            # check if order, exists
            if not order.exists():
                return Response(
                    {
                        "success": False,
                        "message": f'Order with {data.get("id")} not found',
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            order[0].delete()
            return Response(
                {
                    "success": True,
                    "message": f"Order {data.get('id')} deleted successfully",
                },
                status=status.HTTP_200_OK,
            )
        except Exception as error:
            print("Error Delete Order View ===== ", error)
            return Response(
                {
                    "error": str(error),
                    "success": False,
                    "message": f"Failed to delete order {data.get('id')}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
