from django.contrib import admin
from main.models import Sport, Events, SportSlide, EventSlide, Stadiums, Prices


# Register your models here.
admin.site.register(Sport)
admin.site.register(SportSlide)
admin.site.register(Events)
admin.site.register(EventSlide)
admin.site.register(Stadiums)


class PricesAdmin(admin.ModelAdmin):
    list_display = ('name', 'sport', 'stadium', 'price')


admin.site.register(Prices, PricesAdmin)