"""
URL configuration for projetoCrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from rest_framework.urls import urlpatterns as rest_framework_urls
from appCrud.views import home, form, create, view, edit, update, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('form/', form, name='form'),
    
    # Endpoint para criação de carros
    path('create/', create, name='create'),
    
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),

    # Endpoint para atualização de carros
    path('update/<int:pk>/', update, name='update'),
    
    path('delete/<int:pk>/', delete, name='delete'),

    # Incluir URLs do Django REST Framework sob o prefixo 'api/'
    path('api/', include(rest_framework_urls)),
]

urlpatterns += staticfiles_urlpatterns()
