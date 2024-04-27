from django.shortcuts import render
from gestion_users import *


def template(request):
    return render(request, 'base.html')


def un_v_un(request):
    return render(request, 'pages/1v1.html')


def accueil(request):
    return render(request, 'pages/Accueil.html')


def creer_une_equipe(request):
    return render(request, 'pages/Creer_une_equipe.html')


def mon_compte(request):
    return render(request, 'pages/Mon_compte.html')


def leaderboard(request):
    return render(request, 'pages/Leaderboard.html')


def a_propos(request):
    return render(request, 'pages/A_propos.html')


def contact(request):
    return render(request, 'pages/Contact.html')


def page_connection(request):
    return render(request, 'pages/page_connection.html')


def page_inscription(request):
    return render(request, 'pages/page_inscription.html')


from django.contrib import messages


def creer_user_form(request):
    if request.method == 'GET':
        # Handle the GET request
        return render(request, 'pages/accueil.html')
    elif request.method == 'POST':
        # Handle the POST request and process the form data
        username = request.POST.get('username')
        riot_id = request.POST.get('RiotID')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if creer_user(riot_id, username, password, email):
            return render(request, 'pages/accueil.html')
        else:
            messages.error(request, 'Votre compte existe déjà')
            return render(request, 'pages/page_inscription.html')
