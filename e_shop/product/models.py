from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, primary_key=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)

    def __str__(self):
        return self.title


LABEL_CHOICES = (
    ('new', 'Новинка'),
    ('bestseller', 'Хит продаж'),
    ('ordinary', 'Обычный')
)


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    label = models.CharField(max_length=10, choices=LABEL_CHOICES)

    def __str__(self):
        return self.title
