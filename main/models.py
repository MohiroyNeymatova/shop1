from django.db import models

# Create your models here.


class Cash(models.Model):
    money = models.DecimalField(decimal_places=2, max_digits=52)


class Client(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    debt = models.DecimalField(decimal_places=2, max_digits=52, default=0)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250)
    base_price = models.DecimalField(decimal_places=2, max_digits=52)
    selling_price = models.DecimalField(decimal_places=2, max_digits=52)

    def __str__(self):
        return self.name


class Payment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    money = models.DecimalField(decimal_places=2, max_digits=52)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.client.name


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    @property
    def total(self):
        items = OrderItem.objects.filter(order=self)
        total = 0
        for i in items:
            total += i.total
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    @property
    def total(self):
        return self.quantity * self.product.selling_price

