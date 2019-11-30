from django.shortcuts import render
from django.http import HttpResponse
from .models import Sightings, Features, Flowers, Members
from .forms import FlowerForm
from django.http import JsonResponse
from django.core.serializers import serialize

def index(request):
    return render(request, 'index.html')

def flowers(request):
    return render(request, 'flowers.html')

def sightings(request):
    path = request.path.strip('/').split('/')
    if (len(path) == 1):
        return render(request, 'sightings.html', {'form': FlowerForm()})
    else:
        flower_comname = path[1].replace('_', ' ')
        query = 'SELECT * FROM sightings where name like "{}" order by sighted desc limit 10'.format(flower_comname)
        sightings = Sightings.objects.raw(query)
        # for sighting in sightings:
        #     print(sighting.person + sighting.location + sighting.sighted.strftime("%m/%d/%Y"))
        resp = serialize('json', sightings)
        print(resp)
        return HttpResponse(resp)

def log(request):
    return render(request, 'log.html')