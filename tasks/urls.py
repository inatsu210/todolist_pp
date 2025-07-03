from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # La vue task_list gère maintenant la page d'accueil
    path('register/', views.register, name='register'),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('accounts/', include('django.contrib.auth.urls'))
]