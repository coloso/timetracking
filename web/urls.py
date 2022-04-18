from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('persons/', views.persons, name='persons')
]