from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('vae', views.index, name='vae'),
    path('bright', views.bright, name='bright'),
    path('dark', views.dark, name='dark'),
    path('mixed', views.mixed, name='mixed'),
    path('music/<slug:slug>/', views.make_one, name='one'),
    path('bright/<slug:slug>/', views.make_bright, name='make_bright'),
    path('dark/<slug:slug>/', views.make_dark, name='make_dark'),
    path('mixed/<slug:slug>/', views.make_mixed, name='make_miexd'),
    path('save/<slug:type>/<slug:slug>/', views.download, name='download'),
    path('dice', views.dice, name='dice'),
]

