from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_tarefas, name='listar_tarefas'),
    path('criar/', views.criar_tarefa, name='criar_tarefa'),
    path('atualizar/<int:pk>/', views.atualizar_tarefa, name='atualizar_tarefa'),
    path('excluir/<int:pk>/', views.excluir_tarefa, name='excluir_tarefa'),
    
    # ... outras URLs ...
]
