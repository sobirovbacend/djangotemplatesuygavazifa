from django.db import models

class Categories(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.category_name


class Products(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    discontinued = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name


class Order_details(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    order = models.ForeignKey('Orders', on_delete=models.CASCADE)

    def __str__(self):
        return self.product.product_name


class Orders(models.Model):
    order_date = models.DateTimeField(auto_now=True)
    required_date = models.DateTimeField(blank=True, null=True)
    shipped_date = models.DateTimeField(blank=True, null=True)





