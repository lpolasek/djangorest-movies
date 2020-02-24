"""rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from django.views.generic import TemplateView

from rest_framework import routers
from rest_framework.schemas import get_schema_view

from rest import settings
from movies import views


router = routers.DefaultRouter()
router.register(r'persons', views.PersonViewSet)
router.register(r'movies', views.MovieViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path(
        'api-auth/',
        include(
            'rest_framework.urls',
            namespace='rest_framework'
        )
    ),
]

if settings.DEBUG:
    urlpatterns += [
        path(
            'openapi',
            get_schema_view(
                title="Movies",
                description="API for movies app",
                version="1.0.0"
            ), name='openapi-schema'
        ),
        path(
            'swagger-ui/', TemplateView.as_view(
                template_name='swagger-ui.html',
                extra_context={'schema_url': 'openapi-schema'}
            ),
            name='swagger-ui'
        ),
    ]
