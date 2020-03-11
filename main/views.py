from django.shortcuts import render, get_object_or_404
from main.models import Sport, Events, SportSlide, EventSlide, Stadiums, Prices, More, Trainers, Sliders, Images


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
    slider_id = Sliders.objects.get(stadium = stadium_id)
    slides = Images.objects.filter(slider = slider_id).order_by('sort')
    return render(request, 'stadium_detail.html',
                  {'page_title': 'Детальная', 'stadium': stadium, 'sports': stadium.sport.split(','), 'slider_id': slider_id, 'slides': slides})


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
    sports = Sport.objects.order_by('sort').all()
    stadiums = Stadiums.objects.order_by('sort').all()
    return render(request, 'events.html', {'page_title': 'События', 'events': events, 'sports': sports, 'stadiums': stadiums})


def about(request):
    return render(request, 'about.html', {'page_title': 'О лагере'})


def more(request, more_id):
    more_info = get_object_or_404(More, id=more_id)
    trainers = Trainers.objects.order_by('sort').all()
    return render(request, 'more.html', {'page_title': 'Подробнее', 'more': more_info, 'trainers': trainers})


def prices(request):
    sports = Sport.objects.order_by('sort').all()
    stadiums = Stadiums.objects.order_by('sort').all()
    prices = Prices.objects.order_by('sort').all()

    return render(request, 'prices.html',
                  {'page_title': 'Цены', 'prices': prices})

