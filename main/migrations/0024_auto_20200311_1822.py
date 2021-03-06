# Generated by Django 2.0.6 on 2020-03-11 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_more_trainers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='main/images', verbose_name='Изображение')),
                ('sort', models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True)),
            ],
            options={
                'verbose_name': 'Слайдер',
                'verbose_name_plural': 'Слайдеры',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Sliders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('sort', models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True)),
                ('stadium', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Stadiums')),
            ],
            options={
                'verbose_name': 'Слайдер',
                'verbose_name_plural': 'Слайдеры',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='images',
            name='slider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Sliders'),
        ),
    ]
