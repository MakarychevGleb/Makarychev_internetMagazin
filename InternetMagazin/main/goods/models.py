from django.db import models

# Create your models{table} here.
class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

class Products(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=8, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=8, decimal_places=2, verbose_name='Скидка(%)')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Кол-во')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

# decimal_places - кол-во знаков после запятой
# max_digits - кол-во знаков до запятой
# default по умолчанию
# PROTECT - если в категории остался товар категорию не получ. удалить
# CASCADE - если в категории остался товар категория удаляется с предупреждением об удалении товара
# SET_DEFAULT - при удалении категории всем товарам будет присвоено default значение