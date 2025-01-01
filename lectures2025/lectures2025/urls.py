from django.contrib import admin
from django.urls import path
from .views import HomeView, multi_form_view, Perfil_lector, LectorListView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='home'),
    path('afegeix_llibre/', multi_form_view, name='afegir_llibre'),
    path('lectores/', LectorListView.as_view(), name='lector_list'),
    path('perfil/<int:pk>/', Perfil_lector.as_view(), name='perfil'),
]
