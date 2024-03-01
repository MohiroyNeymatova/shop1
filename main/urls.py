from django.urls import path
from .views import *

urlpatterns = [
    path('create_client/', create_client),
    path('get_clients/', get_clients),
    path('get_client_by_id/<int:pk>', get_client_by_id),
    path('get_products/', get_products),
    path('create_payment/', create_payment),
    path('get_payment_by_client/<int:pk>', get_payment_by_client),
    path('create_order/', create_order),
    path('order_item_create/', order_item_create),
    path('get_order_by_client/<int:pk>/', get_order_by_client),
    path('get_order_items/<int:pk>/', get_order_items),
    path('get_order/<int:pk>/', get_order)
]