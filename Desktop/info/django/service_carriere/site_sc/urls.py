from django.urls import path
from . import views


urlpatterns = [
	path('connexion/', views.connexion, name='connexion'),
	path('deconnexion/', views.deconnexion, name='deconnexion'),
	path('accueil/', views.accueil, name='accueil'),
    path('evenement/<int:id>', views.voir, name='voir'),
    path('inscription/', views.inscription, name='inscription'),
    path('inscription_etudiant/', views.inscription_etudiant, name='inscription_etudiant'),
    path('inscription_entreprise/', views.inscription_entreprise, name='inscription_entreprise'),
    path('inscription_administration/', views.inscription_administration, name='inscription_administration'),
    path('gestion_profil/', views.gestion_profil, name='gestion_profil'),
    path('recherche_stage/', views.recherche_stage, name='recherche_stage'),
    path('recherche_entreprise/', views.recherche_entreprise, name='recherche_entreprise'),
    path('proposer_stage/', views.proposer_stage, name='proposer_stage'),
    path('proposer_evenement/', views.proposer_evenement, name='proposer_evenement'),
    path('agenda/', views.agenda, name='agenda'),
]

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)