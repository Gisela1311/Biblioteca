from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.HomeView.as_view(), name='home'),
    path('afegeix_llibre/', views.afegir_llibre.as_view(), name='afegir_llibre'),
    path('perfil/', views.perfil_lector.as_view(), name='perfil'),
]
