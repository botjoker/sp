from django.shortcuts import render, get_object_or_404
from main.models import Sport, Events, SportSlide, EventSlide, Stadiums, Prices


def home(request):
    sports = Sport.objects.order_by('sort').all()
    return render(request, 'index.html', {'page_title': 'Главная', 'sports': sports})


def sport_detail(request, sport_id):
    sport = get_object_or_404(Sport, id=sport_id)
    slides = SportSlide.objects.filter(sport = sport_id).order_by('sort')
    return render(request, 'sport_detail.html', {'page_title': 'Детальная', 'sport': sport, 'slides': slides})


def event_detail(request, event_id):
    event = get_object_or_404(Events, id=event_id)
    slides = EventSlide.objects.filter(event=event_id).order_by('sort')
    return render(request, 'event_detail.html', {'page_title': 'Детальная', 'event': event, 'slides': slides})


def stadium_detail(request, stadium_id):
    stadium = get_object_or_404(Stadiums, id=stadium_id)
    return render(request, 'stadium_detail.html', {'page_title': 'Детальная', 'stadium': stadium, 'sports': stadium.sport.split(',')})


def contacts(request):
    return render(request, 'contacts.html', {'page_title': 'Контакты'})


def map(request):
    return render(request, 'map.html', {'page_title': 'Карта'})


def order(request):
    return render(request, 'order.html', {'page_title': 'Заказ'})


def stadiums(request):
    stadiums = Stadiums.objects.order_by('sort').all()
    return render(request, 'stadiums.html', {'page_title': 'Стадионы', 'stadiums': stadiums})


def events(request):
    events = Events.objects.order_by('sort').all()
    return render(request, 'events.html', {'page_title': 'События', 'events': events})


def about(request):
    return render(request, 'about.html', {'page_title': 'О лагере'})


def prices(request):
    sports = Sport.objects.order_by('sort').all()
    stadiums = Stadiums.objects.order_by('sort').all()
    prices = Prices.objects.order_by('sort').all()
    sections = Prices.objects.order_by('sort').filter(name='Смена')
    days = Prices.objects.order_by('sort').filter(name='День')
    trains = Prices.objects.order_by('sort').filter(name='Тренировка')

    return render(request, 'prices.html',
                  {'page_title': 'Цены', 'prices': prices, 'sports': sports, 'stadiums': stadiums,
                   'days': days, 'sections': sections, 'trains': trains})

