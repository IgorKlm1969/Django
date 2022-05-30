# from tabnanny import verbose
from django.db import models


# from django.db.models import CharField


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название', unique=True)
    description = models.TextField(verbose_name='Описание')

    # class ProductCategory(models.Model):
    #     name: CharField = models.CharField(verbose_name='имя', max_length=64, unique=True)
    #     description = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return f'#{self.pk}.{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категория'
        ordering = ('name', )

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    image=models.ImageField(upload_to='product', blank=True, null=True)
    name = models.CharField(max_length=128, verbose_name='Название')
    short_desk = models.CharField(max_length=128, verbose_name='Краткое описание')
    description = models.TextField(verbose_name='Описание')
    price= models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    def __str__(self):
        return f'{self.name} ({self.category.name})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
