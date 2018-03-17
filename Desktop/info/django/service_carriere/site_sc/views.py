from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import ConnexionForm, InscriptionForm, Inscription_etudiantForm, Inscription_entrepriseForm,Inscription_administrationForm
from django.contrib.auth.decorators import login_required
from .models import Evenement, Domaine


def accueil(request):
    evenements = Evenement.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'site_sc/accueil.html', {'evenements': evenements})

def voir(request, id):
    evenement = get_object_or_404(Evenement, id=id)
    return render(request, 'site_sc/voir.html', {'evenement': evenement})   

def inscription(request):
	test1 = False
	test2 = False
	test3 = False
	form = InscriptionForm(request.POST or None)
	if form.is_valid(): 
		qualité = form.cleaned_data['qualité']
		if qualité == '1':
			test1 = True
		elif qualité == '2':
			test2 = True
		elif qualité == '3':
			test3 = True
	return render(request, 'site_sc/inscription.html', locals())

def inscription_etudiant(request):
	form = Inscription_etudiantForm(request.POST or None)
	if form.is_valid(): 
		username = form.cleaned_data["username"]
		password = form.cleaned_data["password"]
		nom = form.cleaned_data["nom"]
		prénom = form.cleaned_data["prenom"]
		adresse = form.cleaned_data["adresse"]
		mail = form.cleaned_data["mail"]
		notif_stage = form.cleaned_data["notif_stage"]
		notif_evenement = form.cleaned_data["notif_evenement"]
		cv = form.cleaned_data["cv"]
		user = User.objects.create_user(username, mail, password)
		UserEtudiant.objects.create(user=user, nom=nom, prénom=prénom, notif_evenement=notif_evenement, notif_stage=notif_stage, adresse=adresse, mail=mail, cv=cv, qualité='1')
	return render(request, 'site_sc/inscription_etudiant.html', locals())

def inscription_entreprise(request):
	for secteur in Domaine.objects.all() :
		i=1
		secteurs_choices = (i, Domaine.nom)
		i=i+1
	form = Inscription_entrepriseForm(request.POST or None)
	if form.is_valid() and form.cleaned_data["password"]==form.cleaned_data["conf_password"]: 
		username = form.cleaned_data["username"]
		password = form.cleaned_data["password"]
		nom = form.cleaned_data["nom"]
		mail = form.cleaned_data["mail"]
		taille = form.cleaned_data["taille"]
		secteur = form.cleaned_data["secteur"]
		adresse = form.cleaned_data["adresse"]
		User.objects.create_user(username, mail, password)
		UserEntreprise.objects.create(user=user, nom=nom, mail=mail, adresse=adresse, taille=taille, secteur=secteur, qualité='2')
	return render(request, 'site_sc/inscription_entreprise.html', locals())

def inscription_administration(request):
	form = Inscription_administrationForm(request.POST or None)
	if form.is_valid() and form.cleaned_data["password"]==form.cleaned_data["conf_password"]: 
		username = form.cleaned_data["username"]
		password = form.cleaned_data["password"]
		nom = form.cleaned_data["nom"]
		mail = form.cleaned_data["mail"]
		adresse = form.cleaned_data["adresse"]
		user_administration = User.objects.create_user(username, mail, password)
		user_administration.is_staff= True
		UserEntreprise.objects.create(user=user, nom=nom, mail=mail, adresse=adresse, qualité='3')
	return render(request, 'site_sc/inscription_administration.html', locals())


def connexion(request):
    error = False
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur

            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'site_sc/connexion.html', locals())

def deconnexion(request):
    logout(request)
    return render(request, 'site_sc/deconnexion.html', locals())

def agenda(request):
	return render(request, 'site_sc/agenda.html', locals())

def gestion_profil(request):
	return render(request, 'site_sc/gestion_profil.html', locals())
	
def recherche_stage(request):
	return render(request, 'site_sc/recherche_stage.html', locals())

def recherche_entreprise(request):
	return render(request, 'site_sc/recherche_entreprise.html', locals())

def proposer_stage(request):
	return render(request, 'site_sc/proposer_stage.html', locals())

def proposer_evenement(request):
	return render(request, 'site_sc/proposer_evenement.html', locals())



