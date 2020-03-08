# Generated by Django 2.0.6 on 2020-03-04 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_stadiums'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='stadium',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Stadiums'),
        ),
        migrations.AddField(
            model_name='stadiums',
            name='adress',
            field=models.TextField(blank=True, default='', verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='stadiums',
            name='imagebig',
            field=models.ImageField(blank=True, default='', null=True, upload_to='main/images', verbose_name='Изображение большое'),
        ),
        migrations.AddField(
            model_name='stadiums',
            name='metro',
            field=models.CharField(blank=True, default='', max_length=250, verbose_name='Метро'),
        ),
        migrations.AddField(
            model_name='stadiums',
            name='timefrom',
            field=models.DateField(blank=True, null=True, verbose_name='Начало смены'),
        ),
        migrations.AddField(
            model_name='stadiums',
            name='timeto',
            field=models.DateField(blank=True, null=True, verbose_name='Конец смены'),
        ),
    ]