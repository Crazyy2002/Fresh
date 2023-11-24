from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name='название')

    def __str__(self):
        return self.name

class Articles(models.Model):
    title = models.CharField('Название', max_length=100, default='', blank=False)
    date = models.DateField('Дата изготовления')
    date1 = models.DateField('Дата истечения срока годности')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    photo = models.ImageField(upload_to='images/', verbose_name='Фото', blank=True, null=True)
    current_date = models.DateField('Текущая дата', editable=False, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Обновляем поле current_date при каждом сохранении объекта
        self.current_date = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


