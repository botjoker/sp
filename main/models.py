from django.db import models


class Sport(models.Model):
    name = models.CharField(max_length=30, verbose_name='Вид спорта')
    image = models.ImageField('Изображение', upload_to='main/images', default='',blank=True)
    secondimage = models.ImageField('Изображение детальное', upload_to='main/images', default='', blank=True)
    description = models.TextField(verbose_name='Описание',default='',blank=True)
    sort = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

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
    sort = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        verbose_name='Блок для видов спорта'
        verbose_name_plural='Блоки для видов спорта'
        ordering=['id']

    def __str__(self):
        return self.name


class Stadiums(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(verbose_name='Описание', default='', blank=True)
    video = models.TextField(verbose_name='Видео', default='', blank=True)
    image = models.ImageField('Изображение', upload_to='main/images', default='', blank=True, null=True)
    metro = models.CharField(verbose_name='Метро', max_length=250, default='', blank=True)
    adress = models.TextField(verbose_name='Адрес', default='', blank=True)
    timefrom = models.DateField(verbose_name='Начало смены', blank=True, null=True)
    timeto = models.DateField(verbose_name='Конец смены', blank=True, null=True)
    sport = models.CharField(verbose_name='Виды спорта', max_length=250, default='', blank=True)
    coordinates = models.CharField(verbose_name='Координаты', max_length=250, default='', blank=True)
    sort = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        verbose_name='Стадион'
        verbose_name_plural='Стадионы'
        ordering=['id']

    def __str__(self):
        return self.name


class Events(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.SET_NULL, null=True)
    stadium = models.ForeignKey(Stadiums, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=30, verbose_name='Событие')
    image = models.ImageField('Изображение', upload_to='main/images', default='',blank=True)
    secondimage = models.ImageField('Изображение детальное', upload_to='main/images', default='', blank=True)
    description = models.TextField(verbose_name='Описание',default='',blank=True)
    eventDate = models.DateField()
    sort = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

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
    sort = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        verbose_name='Блок для событий'
        verbose_name_plural='Блоки для событий'
        ordering=['id']

    def __str__(self):
        return self.name


class Prices(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.SET_NULL, null=True)
    stadium = models.ForeignKey(Stadiums, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=250)
    price1 = models.DecimalField('Цена за смену', max_digits=5, decimal_places=0, blank=True, null=True)
    price2 = models.DecimalField('Цена за день', max_digits=5, decimal_places=0, blank=True, null=True)
    price3 = models.DecimalField('Цена за тренировку', max_digits=5, decimal_places=0, blank=True, null=True)
    image = models.ImageField('Изображение', upload_to='main/images', default='', blank=True, null=True)
    sort = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        verbose_name='Цена'
        verbose_name_plural='Цены'
        ordering=['id']

    def __str__(self):
        return self.name


class More(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=250)
    video = models.TextField(verbose_name='Видео', default='', blank=True)
    description = models.TextField(verbose_name='Расписание', default='', blank=True)
    sort = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        verbose_name='Подробнее'
        verbose_name_plural='Подробнее'
        ordering=['id']

    def __str__(self):
        return self.name


class Trainers(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.SET_NULL, null=True)
    more = models.ForeignKey(More, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=250)
    image = models.ImageField('Изображение', upload_to='main/images', default='', blank=True, null=True)
    sort = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        verbose_name='Тренер'
        verbose_name_plural='Тренеры'
        ordering=['id']

    def __str__(self):
        return self.name


class Sliders(models.Model):
    stadium = models.ForeignKey(Stadiums, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=250)
    sort = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        verbose_name='Слайдер'
        verbose_name_plural='Слайдеры'
        ordering=['id']

    def __str__(self):
        return self.name

class Images(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    slider = models.ForeignKey(Sliders, on_delete=models.SET_NULL, null=True)
    image = models.ImageField('Изображение', upload_to='main/images', default='', blank=True, null=True)
    sort = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        verbose_name='Изображение слайдера'
        verbose_name_plural='Изображения слайдера'
        ordering=['id']

    def __str__(self):
        return self.name