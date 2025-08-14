from django.urls import path
from .views import AutoresView

urlpatterns = [
    path('autores', AutoresView.as_view())
]
