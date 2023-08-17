from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('staff.html', views.staff, name='staff'), #Toujours mettre le nom de la page.html pour eviter les erreurs 404
    path('vehicules.html', views.vehicules, name='vehicules'),
    path('vehiculearret.html', views.vehiculearret, name='vehiculearret'),
     path('vehiculeoccupe.html', views.vehiculeoccupe, name='vehiculeoccupe'),
    path('profile.html', views.profile, name='profile'),
    
]