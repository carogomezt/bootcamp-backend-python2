from django.db import models

# Create your models here.
class CartItem(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product_name} - ${self.product_price}"