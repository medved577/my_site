from django.db import models
from django.urls import reverse

class Category(models.Model):
    # категории к которым относятся товары
    name =  models.CharField(max_length=150, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])