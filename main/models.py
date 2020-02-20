from django.db import models

class Sport(models.Model):
    name = models.CharField(max_length=30, verbose_name='Вид спорта')
    image = models.ImageField('Изображение', upload_to='main/images', default='',blank=True)

    class Meta:
        verbose_name='Вид спорта'
        verbose_name_plural='Виды спорта'
        ordering=['name']

    def __str__(self):
        return self.name