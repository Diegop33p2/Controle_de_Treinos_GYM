from django.contrib import admin
from django.urls import path
from treino_academia import views


urlpatterns = [
     path('', views.record_list, name='index'),  # Redirecionar para a lista de registros
     path('admin/', admin.site.urls), #pagina adm
    path('records/', views.record_list, name='record_list'),
    path('records/create/', views.record_create, name='record_create'),
    path('records/update/<int:pk>/', views.record_update, name='record_update'),
    path('records/delete/<int:pk>/', views.record_delete, name='record_delete'),

    path('pernas/', views.pernas_list, name='pernas_list'),
    path('pernas/create/', views.pernas_create, name='pernas_create'),
    path('pernas/update/<int:pk>/', views.pernas_update, name='pernas_update'),
    path('pernas/delete/<int:pk>/', views.pernas_delete, name='pernas_delete'),

    path('costas/', views.costas_list, name='costas_list'),
    path('costas/create/', views.costas_create, name='costas_create'),
    path('costas/update/<int:pk>/', views.costas_update, name='costas_update'),
    path('costas/delete/<int:pk>/', views.costas_delete, name='costas_delete')

]


