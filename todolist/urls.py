from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # URLs pour la connexion, déconnexion, etc.
    path('', include('tasks.urls')),  # Vos URLs d'application
]