# Generated by Django 2.0.6 on 2020-03-04 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20200301_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stadiums',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, default='', verbose_name='Описание')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='main/images', verbose_name='Изображение')),
                ('sort', models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True)),
            ],
            options={
                'verbose_name': 'Стадион',
                'verbose_name_plural': 'Стадионы',
                'ordering': ['id'],
            },
        ),
    ]
