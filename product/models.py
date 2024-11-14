from django.db import models

# Create your models here.


class Product(models.Model):

    class SizeOptions(models.TextChoices):
        SMALL = 'S', 'Small'
        MEDIUM = 'M', 'Medium'
        LARGE = 'L', 'Large'
        EXTRA_LARGE = 'XL', 'Extra Large'

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()

    size = models.CharField(
        max_length=2,
        choices=SizeOptions.choices,
        default=SizeOptions.MEDIUM,
    )

    def __str__(self):
        return self.name
