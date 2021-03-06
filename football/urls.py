"""football URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from main import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('sport/<str:sport_id>/', views.sport_detail, name='sport-detail'),
    path('events/<str:event_id>/', views.event_detail, name='event-detail'),
    path('stadiums/<str:stadium_id>/', views.stadium_detail, name='stadium-detail'),
    path('more/<str:more_id>/', views.more, name='more'),
    path('contacts/', views.contacts, name='contacts'),
    path('order/', views.order, name='order'),
    path('map/', views.map, name='map'),
    path('stadiums/', views.stadiums, name='stadiums'),
    path('events/', views.events, name='events'),
    path('about/', views.about, name='about'),
    path('prices/', views.prices, name='prices'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
