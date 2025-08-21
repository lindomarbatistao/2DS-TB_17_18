from django.urls import path
from .views import AutoresView, visualizacao_autor, EditorasView, LivrosView

urlpatterns = [
    path('autores', AutoresView.as_view()), 
    path('authors', visualizacao_autor),
    path('editoras', EditorasView.as_view()),
    path('livros', LivrosView.as_view()),
    
]
