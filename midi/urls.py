from django.urls import path
from . import views

urlpatterns = [
    path('/', views.index, name='index'),
    path('/vae', views.index, name='vae'),
    path('/music', views.make_one, name='one'),
]