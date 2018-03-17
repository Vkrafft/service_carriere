from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser

#modèle des différents domaines des stages
#Ex : electronique, informatique, banque, BTP etc...
class Domaine(models.Model):
	nom = models.CharField(max_length=30)

	def __str__(self):
		return self.nom

#modèle du stage, proposable par les entreprises et les administrations
class Stage(models.Model):
	titre = models.CharField(max_length=200)
	slug = models.SlugField()
	auteur = models.CharField(max_length=100)
	description = models.TextField(null=True)
	remuneration = models.CharField(max_length=20)
	date_parution = models.DateTimeField(verbose_name="Date de parution",
		auto_now_add=True, auto_now=False)
	date_debut = models.DateTimeField(verbose_name="Date de début")
	date_fin = models.DateTimeField(verbose_name="Date de fin")
	duree = models.IntegerField()
	is_visible = models.BooleanField(verbose_name="Article publié ?",
		default=False)
	categorie = models.ForeignKey('Categorie_stage', on_delete=models.CASCADE)
	domaine = models.ForeignKey('Domaine', on_delete=models.CASCADE)

	class Meta:
		verbose_name = "stage"
		ordering = ['date_parution']

		def __str__(self):
			return self.titre

#modèle de l'évènement, proposable par les adminisatations
class Evenement(models.Model):
	titre = models.CharField(max_length=100)
	slug = models.SlugField()
	auteur = models.CharField(max_length=42)
	description = models.TextField(null=True)
	lieu = models.CharField(max_length=200)
	nombre_place = models.IntegerField()
	inscription = models.BooleanField()
	theme = models.CharField(max_length=100)
	date_parution = models.DateTimeField(verbose_name="Date de parution",
		auto_now_add=True, auto_now=False)
	date = models.DateTimeField(verbose_name="Date de l'évènement")
	is_visible = models.BooleanField(verbose_name="Article publié ?",
		default=False)
	type_evenement = models.ForeignKey('Type_evenement', on_delete=models.CASCADE)
	image = models.ImageField(null=True, blank=True, upload_to="image_evenement/")

	class Meta:
		verbose_name = "évènement"
		ordering = ['date']

		def __str__(self):
			return self.titre

#modèle des différentes catégories de stages disponibles à la proposition
#Ex : stage 1A, stage 2A, stage de fin d'étude etc...
class Categorie_stage(models.Model):
	nom = models.CharField(max_length=30)

	def __str__(self):
		return self.nom

#modèle des différents types dévènement proposables
#Ex : café rencontre, visite d'entreprise, conférence etc...
class Type_evenement(models.Model):
	nom = models.CharField(max_length=30)

	def __str__(self):
		return self.nom



class Institution(models.Model):
	nom = models.CharField(max_length=30)

	def __str__(self):
		return self.nom

#modèles définissant les différents utilisateurs du site		
class UserEtudiant(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)  # La liaison OneToOne vers le modèle User
	institution = models.ForeignKey('Institution', on_delete=models.CASCADE)
	avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
	nom = models.CharField(max_length=255)
	prénom = models.CharField(max_length=255)
	notif_stage = models.BooleanField()
	notif_evenement = models.BooleanField()
	adresse = models.CharField(max_length=255, default="")
	cv = models.FileField(null=True, blank=True, upload_to="CVs/")
	qualité = models.IntegerField()


	def __str__(self):
		return "Profil de {0}".format(self.user.username)

class UserInstitution(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # La liaison OneToOne vers le modèle User
    nom = models.CharField(max_length=255)
    institution = models.ForeignKey('Institution', on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
    signature = models.TextField(blank=True)
    adresse = models.CharField(max_length=255, default="")
    qualité = models.IntegerField()
    

    def __str__(self):
    	return "Profil de {0}".format(self.user.username)

class UserEntreprise(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # La liaison OneToOne vers le modèle User
    nom = models.CharField(max_length=255)
    domaine = models.ForeignKey('Domaine', on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
    signature = models.TextField(blank=True)
    taille = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255, default="")
    qualité = models.IntegerField()


    def __str__(self):
    	return "Profil de {0}".format(self.user.username)

