from django.shortcuts import render
from django.http import HttpResponse
from .models import Sightings, Features, Flowers, Members
from .forms import FlowerSelectForm, FlowerInformationForm, NewSightingForm
from django.http import JsonResponse
from django.core.serializers import serialize
from django.db import connection
import datetime

def index(request):
    return render(request, 'index.html')

def flowers(request):
    if request.method == 'GET':
        path = request.path.strip('/').split('/')
        if (len(path) == 1):
            return render(request, 'flowers.html', {'flower_select_form': FlowerSelectForm(), 'flower_information_form': FlowerInformationForm()})
        else:
            flower_comname = path[1].replace('_', ' ')
            flowers = Flowers.objects.raw('SELECT * FROM flowers where comname like :comname limit 1', {"comname": flower_comname})

            data = []
            for flower in flowers:
                data += [
                            { 
                                'genus' : flower.genus,
                                'species' : flower.species,
                                'comname' : flower.comname,
                            } 
                        ]
            return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        comname = request.POST.get("flowers", "")
        new_genus = request.POST.get("genus", "")
        new_species = request.POST.get("species", "")

        with connection.cursor() as cursor:
            query = "UPDATE flowers SET genus = :genus, species = :species WHERE comname= :comname"
            cursor.execute(
                query,
                {
                    "genus": new_genus,
                    "species": new_species,
                    "comname": comname
                }
            )

        return render(request, 'flowers.html', {'flower_select_form': FlowerSelectForm(), 'flower_information_form': FlowerInformationForm()})

def sightings(request):
    path = request.path.strip('/').split('/')
    if (len(path) == 1):
        return render(request, 'sightings.html', {'flower_select_form': FlowerSelectForm()})
    else:
        flower_comname = path[1].replace('_', ' ')
        sightings = Sightings.objects.raw('SELECT * FROM sightings where name like :comname order by sighted desc limit 10', {"comname": flower_comname})
        data = []
        for sighting in sightings:
            data += [
                        { 
                            'person' : sighting.person,
                            'location' : sighting.location,
                            'sighted' : sighting.sighted.strftime("%m/%d/%Y")
                        } 
                    ]
        return JsonResponse(data, safe=False)

def log(request):
    if request.method == 'GET':
        return render(request, 'log.html', {'flower_select_form': FlowerSelectForm(), 'new_sighting_form': NewSightingForm()})
    elif request.method == 'POST':
        name = request.POST.get("flowers", "")
        person = request.POST.get("person", "")
        location = request.POST.get("location", "")
        
        sighted_month = request.POST.get("sighted_month", "")
        sighted_day = request.POST.get("sighted_day", "")
        sighted_year = request.POST.get("sighted_year", "")
        sighted = "{}-{}-{}".format(sighted_year, sighted_month, sighted_day)

        with connection.cursor() as cursor:
            query = "INSERT INTO SIGHTINGS VALUES (:name, :person, :location, :sighted)"
            cursor.execute(
                query,
                {
                    "name": name,
                    "person": person,
                    "location": location,
                    "sighted": sighted
                }
            )

        return render(request, 'log.html', {'flower_select_form': FlowerSelectForm(), 'new_sighting_form': NewSightingForm()})