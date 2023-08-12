from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('staff.html', views.staff, name='staff'), #Toujours mettre le nom de la page.html pour eviter les erreurs 404
    
]