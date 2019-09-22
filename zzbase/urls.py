from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework import routers
from pcp_registro_op.api.viewsets import RegistroOpViewSet
from pcp_registro_entrega.api.viewsets import RegistroEntregaViewSet


router = routers.DefaultRouter()
router.register(r'pcp-registro-op', RegistroOpViewSet)
router.register(r'pcp-registro-entrega', RegistroEntregaViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('admin/', admin.site.urls),
]
