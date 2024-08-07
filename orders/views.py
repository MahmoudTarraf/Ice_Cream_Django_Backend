from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer  # Assuming you have the serializer

@api_view(['POST'])
def createOrder(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def getOrderByEmail(request, email):
    orders = Order.objects.filter(email=email)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)
        
@api_view(['GET'])        
def getAllOrders(request):
    orders=Order.objects.all()
    serializer=OrderSerializer(orders,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def update_order(request):
    email = request.data.get('email')
    operation_number = request.data.get('operationNumber')

    try:
        order = Order.objects.get(email=email, operationNumber=operation_number)
    except Order.DoesNotExist:
        return Response({'message': 'Order not found.'}, status=404)

    serializer = OrderSerializer(order, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Order updated successfully.'}, status=200)
    else:
        return Response(serializer.errors, status=400)