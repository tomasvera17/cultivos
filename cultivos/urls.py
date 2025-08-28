from django.urls import path
from .views import listar_cultivos

urlpatterns = [
    path('', listar_cultivos, name='listar_cultivos')
]
