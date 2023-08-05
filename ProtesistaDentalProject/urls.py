"""
URL configuration for ProtesistaDentalProject project.

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
from django.shortcuts import redirect
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from blog import views


urlpatterns = [
    path('', views.inicio_view, name='inicio'),
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path('login/', LoginView.as_view(template_name='blog/user_login.html'), name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)