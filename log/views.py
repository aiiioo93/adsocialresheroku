from datetime import datetime, timedelta

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True  # you can customize other fields here
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('log:home'))
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('log:home'))

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return HttpResponseRedirect(reverse('log:home'))
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('log:login'))

def forgot_password(request):
    if request.method == "POST":
        # Ajoutez ici la logique pour traiter la demande de réinitialisation du mot de passe
        pass
    return render(request, 'forgot.html')



@login_required
def home(request):
    # Vérifier si la variable de session existe
    last_activity = request.session.get('last_activity')
    if last_activity:
        # Convertir la chaîne de caractères en date/heure
        last_activity = datetime.strptime(last_activity, '%Y-%m-%d %H:%M:%S.%f')
        # Calculer la durée depuis la dernière activité
        duration = datetime.now() - last_activity
        if duration > timedelta(minutes=5):
            # Si l'utilisateur a été inactif pendant plus de 5 minutes, le déconnecter
            logout(request)
            return redirect('login')

    # Stocker l'heure de la dernière activité dans la variable de session
    request.session['last_activity'] = str(datetime.now())

    # Votre code pour la vue home ici
    # ...
    return render(request, 'home.html')
