from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('sightings', views.sightings, name='sightings'),
    url('flowers', views.flowers, name='flowers'),
    url('log', views.log, name='log'),
    url('', views.index, name='index'),
]