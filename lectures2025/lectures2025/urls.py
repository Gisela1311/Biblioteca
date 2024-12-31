from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('add_llibre/', views.add_llibre, name='add_llibre'),
    path('perfil/<int:prop_id>/', views.perfil, name='perfil'),
]
