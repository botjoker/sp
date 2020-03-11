from django.contrib import admin
from main.models import Sport, Events, SportSlide, EventSlide, Stadiums, Prices, Trainers, More, Sliders, Images


# Register your models here.
admin.site.register(Sport)
admin.site.register(SportSlide)
admin.site.register(Events)
admin.site.register(EventSlide)
admin.site.register(Stadiums)
admin.site.register(Trainers)
admin.site.register(More)



class PricesAdmin(admin.ModelAdmin):
    list_display = ('name', 'sport', 'stadium', 'price1', 'price2', 'price3')


admin.site.register(Prices, PricesAdmin)


admin.site.register(Sliders)
admin.site.register(Images)
