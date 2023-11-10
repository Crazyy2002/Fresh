from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name='название')

    def __str__(self):
        return self.name

class Articles(models.Model):
    title = models.CharField('Название', max_length=100, default='', blank=False)
    date = models.DateTimeField('Дата изготовления')
    date1 = models.DateTimeField('Дата истечения срока годности')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    photo = models.ImageField(upload_to='images/', verbose_name='Фото', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
