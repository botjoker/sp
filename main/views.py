from django.shortcuts import render, get_object_or_404
from main.models import Sport

def home(request):
    sports = Sport.objects.all()
    return render(request, 'index.html', {'page_title': 'Главная', 'sports': sports})

def sport_detail(request, sport_id):
    sport = get_object_or_404(Sport, id=sport_id)
    return render(request, 'sport_detail.html', {'page_title': 'Детальная', 'sport': sport})

def contacts(request):
    return render(request, 'contacts.html', {'page_title': 'Контакты'})

def map(request):
    return render(request, 'map.html', {'page_title': 'Карта'})

def stadiums(request):
    return render(request, 'stadiums.html', {'page_title': 'Стадионы'})

def events(request):
    return render(request, 'events.html', {'page_title': 'События'})

def about(request):
    return render(request, 'about.html', {'page_title': 'О лагере'})

def prices(request):
    return render(request, 'prices.html', {'page_title': 'Цены'})

