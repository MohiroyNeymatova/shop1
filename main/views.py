from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
from decimal import *


@api_view(["POST"])
def create_client(request):
    Client.objects.create(name=request.POST['name'], phone=request.POST['phone'])
    return Response({'success': True})


@api_view(['GET'])
def get_clients(request):
    return Response(ClientSerializer(Client.objects.all(), many=True).data)


@api_view(['GET'])
def get_client_by_id(request, pk):
    return Response(ClientSerializer(Client.objects.get(id=pk), many=False).data)


@api_view(['GET'])
def get_products(request):
    return Response(ProductSerializer(Product.objects.all(), many=True).data)


@api_view(['POST'])
def create_payment(request):
    client_id = request.POST['client']
    money = request.POST['money']
    client = Client.objects.get(id=client_id)
    Payment.objects.create(client=client, money=money)
    client.debt -= Decimal(money)
    if Cash.objects.all().count() > 0:
        cash = Cash.objects.last()
        cash.money += Decimal(money)
        cash.save()
    else:
        Cash.objects.create(money=money)
    client.save()
    return Response({"payment": True})


@api_view(['GET'])
def get_payment_by_client(request, pk):
    return Response(PaymentSerializer(Payment.objects.filter(client_id=pk), many=True).data)


@api_view(['POST'])
def create_order(request):
    client = Client.objects.get(id=request.POST['client'])
    Order.objects.create(client=client)
    return Response({"success": True})


@api_view(['POST'])
def order_item_create(request):
    order = request.POST['order']
    product = request.POST['product']
    quantity = request.POST['quantity']
    order_item = OrderItem.objects.create(order_id=order, product_id=product, quantity=quantity)
    client = order.client
    debt = client.debt
    debt += order_item.total
    client.save()
    return Response({"success": True})


@api_view(['GET'])
def get_order_by_client(request, pk):
    return Response(OrderSerializer(Order.objects.filter(client_id=pk), many=True).data)


@api_view(['GET'])
def get_order_items(request, pk):
    return Response(OrderItemSerializer(OrderItem.objects.filter(order_id=pk), many=True).data)


@api_view(['GET'])
def get_order(request, pk):
    return Response(OrderSerializer(Order.objects.get(id=pk), many=False).data)
