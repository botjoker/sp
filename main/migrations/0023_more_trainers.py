# Generated by Django 2.0.6 on 2020-03-09 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20200309_2102'),
    ]

    operations = [
        migrations.CreateModel(
            name='More',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('video', models.TextField(blank=True, default='', verbose_name='Видео')),
                ('description', models.TextField(blank=True, default='', verbose_name='Расписание')),
                ('sort', models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True)),
                ('sport', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Sport')),
            ],
            options={
                'verbose_name': 'Подробнее',
                'verbose_name_plural': 'Подробнее',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Trainers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='main/images', verbose_name='Изображение')),
                ('sort', models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True)),
                ('more', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.More')),
                ('sport', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Sport')),
            ],
            options={
                'verbose_name': 'Тренер',
                'verbose_name_plural': 'Тренеры',
                'ordering': ['id'],
            },
        ),
    ]
