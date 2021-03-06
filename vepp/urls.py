"""vepp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path, include

import mainapp.views as mainapp
# import adminapp.views as adminapp

urlpatterns = [
    re_path(r'^auth/', include('authapp.urls', namespace='auth')),
    re_path(r'^$', mainapp.main, name='main'),
    # re_path(r'^main/', include('mainapp.urls', namespace='main')),
    re_path(r'^admin/', include('adminapp.urls', namespace='admin')),
    re_path(r'^crm/', include('crmapp.urls', namespace='crm')),
    # re_path(r'^admin/', adminapp.main_view, name='admin'),
    # re_path(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
