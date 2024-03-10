from django.contrib import admin
from django.urls import path
from treino_academia import views

urlpatterns = [
     path('', views.record_list, name='index'),  # Redirecionar para a lista de registros
    path('records/', views.record_list, name='record_list'),
    path('records/create/', views.record_create, name='record_create'),
    path('records/update/<int:pk>/', views.record_update, name='record_update'),
    path('records/delete/<int:pk>/', views.record_delete, name='record_delete'),
]
