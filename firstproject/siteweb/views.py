from django.shortcuts import render
import random

def accueil(request):
    return render(request, 'accueil.html')

def simulation(request):
    de1 = random.randint(1, 6)
    de2 = random.randint(1, 6)

    egal = (de1 == de2)

    historique = request.session.get('historique', [])

    historique.append({
        'de1': de1,
        'de2': de2,
        'resultat': 'Égaux' if egal else 'Différents'
    })

    request.session['historique'] = historique

    return render(request, 'simulation.html', {
        'de1': de1,
        'de2': de2,
        'egal': egal,
        'historique': historique
    })

def exceptions(request):
    return render(request, 'exceptions.html')

def poo(request):
    return render(request, 'poo.html')