"""voluntAR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from principal.viewsets import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cuentas', AccountViewSet)
router.register(r'eventos', EventViewSet)
router.register(r'aportes', BackViewSet)
router.register(r'aporte_elemento', BackElementViewSet)
router.register(r'aporte_voluntario', EventVoluntaryViewSet)
router.register(r'inscripcion_aporte', EventBackViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/', include('djoser.urls.authtoken'))
]
