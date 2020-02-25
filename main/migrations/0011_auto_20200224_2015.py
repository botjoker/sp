# Generated by Django 2.0.6 on 2020-02-24 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200224_2009'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sportslide',
            options={'ordering': ['id'], 'verbose_name': 'Блок для видов спорта', 'verbose_name_plural': 'Блоки для видов спорта'},
        ),
        migrations.AlterField(
            model_name='sportslide',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='main/images', verbose_name='Изображение'),
        ),
    ]
