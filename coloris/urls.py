from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_note, name='add_note'),
    path('delete_entrys/', views.delete_entrys, name='delete_entrys'),
]