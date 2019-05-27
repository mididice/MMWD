from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('vae', views.index, name='vae'),
    path('music/<slug:slug>/', views.make_one, name='one'),
]

