from django.db import models
from django.utils.text import slugify


class Phone(models.Model):

    name = models.CharField(max_length=100, verbose_name="Модель")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.URLField(max_length=250, verbose_name="Изображение")
    release_date = models.DateField(verbose_name="Дата выпуска")
    lte_exists = models.BooleanField(default=False, verbose_name="Наличие LTE")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL-адрес")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name