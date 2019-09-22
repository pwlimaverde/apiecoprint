from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework import routers
from pcp_registro_op.api.viewsets import RegistroOpViewSet
from pcp_registro_entrega.api.viewsets import RegistroEntregaViewSet
from pcp_upload_xls.api.viewsets import UploadListOpViewSet


router = routers.DefaultRouter()
router.register(r'pcp-registro-op', RegistroOpViewSet)
router.register(r'pcp-registro-entrega', RegistroEntregaViewSet)
router.register(r'pcp-upload-xls', UploadListOpViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('admin/', admin.site.urls),
]
