from django import forms
from .models import Domaine, UserInstitution, UserEtudiant, UserEntreprise

#formulaire de connexion
class ConnexionForm(forms.Form):
	username = forms.CharField(label="Nom d'utilisateur", max_length=30)
	password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

#choix possibles dans l'inscription en temps que qualité
MY_CHOICES = (
	('1', 'Etudiant'),
	('2', 'Entreprise'),
	('3', 'Administration'),
)

#formulaire de préinscription
class InscriptionForm(forms.Form):
	qualité = forms.ChoiceField(choices=(MY_CHOICES))

#formulaire d'inscription etudiant
class Inscription_etudiantForm(forms.Form):
	username = forms.CharField(label="Nom d'utilisateur", max_length=30)
	nom = forms.CharField(label="Nom", max_length=255)
	prénom = forms.CharField(label="Prénom", max_length=255)
	adresse = forms.CharField(widget=forms.Textarea)
	mail = forms.EmailField()
	password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
	conf_password = forms.CharField(label="Confirmez votre Mot de passe", widget=forms.PasswordInput)
	notif_stage = forms.BooleanField(help_text="Notification de stages")
	notif_evenement = forms.BooleanField(help_text="Notification d'évènements")
	cv = forms.FileField(label="votre CV (optionnel)")

	def clean(self):
		cleaned_data = super(Inscription_etudiantForm, self).clean()
		mail = cleaned_data.get('mail')
		password = cleaned_data.get('password')
		conf_password = cleaned_data.get('conf_password')
		if mail:
			pass
		else:
			raise forms.ValidationError("Veuillez entrer une adresse mail valide")
		if password==conf_password:
			pass
		else:
			raise forms.ValidationError("Les deux mots de passe doivent être identiques")
		return cleaned_data
	


secteurs_choices = (
	('1', 'Informatique'),
	('2', 'PME'),
	('3', 'ETI'),
	('4', 'GE'),
	)

#choix dans la taille de l'entreprise
taille_choices = (
	('1', 'TPE'),
	('2', 'PME'),
	('3', 'ETI'),
	('4', 'GE'),
	)

#formulaire d'inscription entreprise
class Inscription_entrepriseForm(forms.Form):
	username = forms.CharField(label="Nom d'utilisateur", max_length=30)
	nom = forms.CharField()
	secteur = forms.ChoiceField(choices=secteurs_choices)
	taille_ = forms.ChoiceField(choices=taille_choices)
	mail = forms.EmailField()
	adresse = forms.CharField(widget=forms.Textarea)
	password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
	conf_password = password = forms.CharField(label="Confirmez votre Mot de passe", widget=forms.PasswordInput)

	def clean(self):
		cleaned_data = super(Inscription_etudiantForm, self).clean()
		mail = cleaned_data.get('mail')
		password = cleaned_data.get('password')
		conf_password = cleaned_data.get('conf_password')
		if mail:
			pass
		else:
			raise forms.ValidationError("Veuillez entrer une adresse mail valide")
		if password==conf_password:
			pass
		else:
			raise forms.ValidationError("Les deux mots de passe doivent être identiques")
		return cleaned_data


#formulaire d"inscritpion adminisatration
class Inscription_administrationForm(forms.Form):
	username = forms.CharField(label="Nom d'utilisateur", max_length=30)
	nom = forms.CharField()
	mail = forms.EmailField()
	adresse = forms.CharField(widget=forms.Textarea)
	password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
	conf_password = password = forms.CharField(label="Confirmez votre Mot de passe", widget=forms.PasswordInput)

	def clean(self):
		cleaned_data = super(Inscription_etudiantForm, self).clean()
		mail = cleaned_data.get('mail')
		password = cleaned_data.get('password')
		conf_password = cleaned_data.get('conf_password')
		if mail:
			pass
		else:
			raise forms.ValidationError("Veuillez entrer une adresse mail valide")
		if password==conf_password:
			pass
		else:
			raise forms.ValidationError("Les deux mots de passe doivent être identiques")
		return cleaned_data
