from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Cash)
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Payment)
admin.site.register(Order)
admin.site.register(OrderItem)
