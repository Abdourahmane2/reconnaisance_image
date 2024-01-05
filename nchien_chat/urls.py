# chien_chat/urls.py
from django.urls import path
from .views import home

urlpatterns = [
    path('home/', home, name='home'),
    # Ajoutez d'autres chemins si nécessaire
]