"""
URL configuration for django_site project.

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
from django.conf import settings
from rest_framework import routers
from my_app.api_views import TagViewSet, ProfessionViewSet

router = routers.DefaultRouter()
router.register(r'tags', TagViewSet)
router.register(r'professions', ProfessionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_app.urls', namespace='my_app')),
    path('users/', include('usersapp.urls', namespace='users')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v0/', include(router.urls))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns