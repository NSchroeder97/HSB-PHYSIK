from django.contrib import admin
from django.urls import path, include
from . import views, experiments_urls, auth

urlpatterns = [
    path('', views.index, name="index"),
    #----------------------------------------
    #path('<int:id>', views.index, name="index"),
    path('register/', auth.register, name="register"),
    path('login/', auth.auth_login, name="login"),
    path('logout/', auth.signout, name="logout"),
    #-----------------------------------------
    path('experiments', views.experiments, name="experiments"),
    path('projects', views.projects, name="projects"),
    path('impressum', views.impressum, name="impressum"),
	path('Labore', views.Labore, name="Labore"),
    path('Mitarbeiter', views.Mitarbeiter, name="Mitarbeiter"),
    path('register', views.register, name="register"),
	
    path('experiments/doppelspalt', experiments_urls.doppelspalt, name="experiments_doppelspalt"),
    path('api/experiments/doppelspalt/<int:lam>/<int:b>/<int:d>/<int:angle>', experiments_urls.doppelspalt_api, name="api_experiments_doppelspalt"),
    
    path('experiments/laser-emissions', experiments_urls.laser_emissions, name="experiments_laser_emissions"),
    path('api/experiments/laser-emissions/<int:n_atoms>/<int:n_photons>/<int:niveau>', experiments_urls.laser_emissions_api, name="api_experiments_laser_emissions")
]
  
