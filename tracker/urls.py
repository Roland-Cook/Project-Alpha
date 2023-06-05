"""
URL configuration for tracker project.

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
from django.urls import path, include
from projects.urls import urlpatterns
from django.shortcuts import redirect
from accounts.urls import urlpattern
from tasks.urls import urlpatternss

urlpatterns = [
    path('', lambda req: redirect('list_projects'), name="home"),
    path("projects/", include(urlpatterns)),
    path("admin/", admin.site.urls),
    path("accounts/", include(urlpattern)),
    path("tasks/", include(urlpatternss))
]
