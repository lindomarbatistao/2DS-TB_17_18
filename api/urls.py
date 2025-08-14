from django.urls import path
from .views import AutoresView, visualizacao_autor

urlpatterns = [
    path('autores', AutoresView.as_view()), 
    path('authors', visualizacao_autor)
]
