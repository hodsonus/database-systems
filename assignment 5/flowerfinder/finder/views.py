from django.shortcuts import render
from django.http import HttpResponse
from .models import Sightings, Features, Flowers, Members
from .forms import FlowerSelectForm, FlowerInformationForm, NewSightingForm
from django.http import JsonResponse
from django.core.serializers import serialize
from django.db import connection

def index(request):
    return render(request, 'index.html')

def flowers(request):
    if request.method == 'GET':
        path = request.path.strip('/').split('/')
        if (len(path) == 1):
            return render(request, 'flowers.html', {'flower_select_form': FlowerSelectForm(), 'flower_information_form': FlowerInformationForm()})
        else:
            flower_comname = path[1].replace('_', ' ')
            query = 'SELECT * FROM flowers where comname like "{}" limit 1'.format(flower_comname)
            flowers = Flowers.objects.raw(query)

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

        cursor = connection.cursor()
        query = "UPDATE flowers SET genus = \"{}\", species=\"{}\" WHERE comname=\"{}\"".format(new_genus, new_species, comname)
        cursor.execute(query)

        return render(request, 'flowers.html', {'flower_select_form': FlowerSelectForm(), 'flower_information_form': FlowerInformationForm()})

def sightings(request):
    path = request.path.strip('/').split('/')
    if (len(path) == 1):
        return render(request, 'sightings.html', {'flower_select_form': FlowerSelectForm()})
    else:
        flower_comname = path[1].replace('_', ' ')
        query = 'SELECT * FROM sightings where name like "{}" order by sighted desc limit 10'.format(flower_comname)
        sightings = Sightings.objects.raw(query)
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
        sighted = request.POST.get("sighted", "")

        cursor = connection.cursor()
        query = "INSERT INTO SIGHTINGS VALUES (\"{}\", \"{}\", \"{}\", \"{}\")".format(name, person, location, sighted)
        # print(query)
        cursor.execute(query)

        return render(request, 'log.html', {'flower_select_form': FlowerSelectForm(), 'new_sighting_form': NewSightingForm()})