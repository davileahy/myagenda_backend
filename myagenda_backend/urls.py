"""
URL configuration for myagenda_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Endpoints de autenticação via API
    path('api/auth/', include('dj_rest_auth.urls')),  # Login, logout, reset de senha, etc.
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),  # Registro de usuários
    # Login: POST /api/auth/login/
    # Logout: POST /api/auth/logout/
    # Registro: POST /api/auth/registration/
    # Reset de senha: POST /api/auth/password/reset/

        # Endpoints para JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # apps
    path('api/', include('agenda.urls'))
]
