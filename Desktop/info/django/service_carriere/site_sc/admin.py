from django.contrib import admin
from site_sc.models import Stage, Evenement, Categorie_stage, Domaine, Type_evenement, Institution, UserEtudiant, UserEntreprise, UserInstitution

class StageAdmin(admin.ModelAdmin):
	list_display   = ('titre', 'auteur', 'date_parution', 'date_debut', 'date_fin', 'domaine')
	list_filter    = ('auteur','categorie', 'duree' ,'date_parution' , 'date_debut', 
		'date_fin', 'domaine', 'remuneration')
	date_hierarchy = 'date_parution'
	ordering       = ('date_parution', )
	search_fields  = ('auteur','categorie', 'duree' ,'date_parution' , 'date_debut', 
		'date_fin', 'domaine', 'remuneration')
	prepopulated_fields = {'slug': ('titre', ), }

class EvenementAdmin(admin.ModelAdmin):
	list_display   = ('titre', 'auteur', 'date', 'lieu', 'theme', 'type_evenement' )
	list_filter    = ('titre', 'auteur', 'date', 'lieu', 'theme', 'type_evenement' )
	date_hierarchy = 'date_parution'
	ordering       = ('date_parution', )
	search_fields  = ('titre', 'auteur', 'date', 'lieu', 'theme','type_evenement' )
	prepopulated_fields = {'slug': ('titre', ), }

class UserEtudiantAdmin(admin.ModelAdmin):
	list_display   = ('nom', 'prénom', 'institution')
	list_filter    = ('nom', 'prénom', 'institution')
	search_fields  = ('nom', 'prénom', 'institution', 'user.username')

class UserInstitutionAdmin(admin.ModelAdmin):
	list_display   = ('institution', 'nom')
	list_filter    = ('institution', 'nom')
	search_fields  = ('institution', 'nom')

class UserEntrepriseAdmin(admin.ModelAdmin):
	list_display   = ('nom', 'taille', 'domaine')
	list_filter    = ('nom', 'taille', 'domaine')
	search_fields  = ('nom', 'taille', 'domaine', 'user.username')


admin.site.register(Stage, StageAdmin)
admin.site.register(Evenement, EvenementAdmin)
admin.site.register(Categorie_stage)
admin.site.register(Type_evenement)
admin.site.register(Domaine)
admin.site.register(Institution)
admin.site.register(UserEtudiant, UserEtudiantAdmin)
admin.site.register(UserEntreprise, UserEntrepriseAdmin)
admin.site.register(UserInstitution, UserInstitutionAdmin)