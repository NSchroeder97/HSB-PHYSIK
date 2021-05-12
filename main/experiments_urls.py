from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from . import experiments

# Doppelspalt
def doppelspalt(response):
    return render(response, 'main/experiments/doppelspalt/index.html')

# Return the data
def doppelspalt_api(response, lam, b, d, angle):
    data = experiments.doppelspalt.doppel_data(lam, b, d, angle)
    return JsonResponse(data, safe=False)

def laser_emissions(response):
    return render(response, 'main/experiments/laser_emissions/index.html')

def laser_emissions_api(response, n_atoms, n_photons, niveau):
    data = experiments.laser_emissions.level_emissions(n_atoms, n_photons, niveau)
    return JsonResponse(data, safe=False)