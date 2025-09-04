from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    # GET / POST
    path('authors', visualizacao_autor),
    path('autores', AutoresView.as_view()), 
    path('editoras', EditorasView.as_view()),
    path('livros', LivrosView.as_view()),
    path('buscar/', AutoresView.as_view()),
    
    # UPDATE / DELETE
    path('autor/<int:pk>', AutoresDetailView.as_view()), 
    path('editora/<int:pk>', EditorasDetailView.as_view()),
    path('livro/<int:pk>', LivrosDetailView.as_view()),

    # TOKEN
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
