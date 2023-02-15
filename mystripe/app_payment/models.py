from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.name

    def true_price(self):
        price = self.price / 100
        return f'{price:.2f}'
