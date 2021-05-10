from django.contrib import admin
from django.urls import path, include
from . import views, experiments, auth

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
    path('experiments/doppelspalt', experiments.doppelspalt, name="experiments_doppelspalt"),
    path('api/experiments/doppelspalt/<int:lam>/<int:b>/<int:d>/<int:angle>', experiments.doppelspalt_api, name="api_experiments_doppelspalt")
]
  
