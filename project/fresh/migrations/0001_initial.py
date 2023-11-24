# Generated by Django 4.2.6 on 2023-11-24 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='название')),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, verbose_name='Название')),
                ('date', models.DateField(verbose_name='Дата изготовления')),
                ('date1', models.DateField(verbose_name='Дата истечения срока годности')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Фото')),
                ('current_date', models.DateField(blank=True, editable=False, null=True, verbose_name='Текущая дата')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fresh.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
