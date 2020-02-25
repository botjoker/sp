from django.db import models


class Sport(models.Model):
    name = models.CharField(max_length=30, verbose_name='Вид спорта')
    image = models.ImageField('Изображение', upload_to='main/images', default='',blank=True)
    secondimage = models.ImageField('Изображение детальное', upload_to='main/images', default='', blank=True)
    description = models.TextField(verbose_name='Описание',default='',blank=True)

    class Meta:
        verbose_name='Вид спорта'
        verbose_name_plural='Виды спорта'
        ordering=['name']

    def __str__(self):
        return self.name


class SportSlide(models.Model):
    sport = models.ForeignKey(Sport, on_delete = models.SET_NULL, null=True)
    name = models.CharField(max_length=250)
    description = models.TextField(verbose_name='Описание', default='', blank=True)
    image = models.ImageField('Изображение', upload_to='main/images', default='', blank=True, null=True)

    class Meta:
        verbose_name='Блок для видов спорта'
        verbose_name_plural='Блоки для видов спорта'
        ordering=['id']

    def __str__(self):
        return self.name


class Events(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=30, verbose_name='Событие')
    image = models.ImageField('Изображение', upload_to='main/images', default='',blank=True)
    secondimage = models.ImageField('Изображение детальное', upload_to='main/images', default='', blank=True)
    description = models.TextField(verbose_name='Описание',default='',blank=True)
    eventDate = models.DateField()

    class Meta:
        verbose_name='Событие'
        verbose_name_plural='События'
        ordering=['name']

    def __str__(self):
        return self.name

class EventSlide(models.Model):
    event = models.ForeignKey(Events, on_delete = models.SET_NULL, null=True)
    name = models.CharField(max_length=250)
    description = models.TextField(verbose_name='Описание', default='', blank=True)
    image = models.ImageField('Изображение', upload_to='main/images', default='', blank=True, null=True)

    class Meta:
        verbose_name='Блок для событий'
        verbose_name_plural='Блоки для событий'
        ordering=['id']

    def __str__(self):
        return self.name
