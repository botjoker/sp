from django.contrib import admin
from main.models import Sport, Events, SportSlide, EventSlide


# Register your models here.
admin.site.register(Sport)
admin.site.register(SportSlide)
admin.site.register(Events)
admin.site.register(EventSlide)