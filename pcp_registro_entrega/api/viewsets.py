from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import (
    IsAuthenticated, IsAdminUser, DjangoModelPermissions,
    IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly
)
from rest_framework.viewsets import ModelViewSet
from pcp_registro_entrega.models import RegistroEntrega
from .serializers import RegistroEntregaSerializer


class RegistroEntregaViewSet(ModelViewSet):

    queryset = RegistroEntrega.objects.all().order_by('op__prev_entrega')
    serializer_class = RegistroEntregaSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    #filterset_fields = ('cliente', 'servico', 'quant')
    filter_backends = (SearchFilter, )
    search_fields = ['id', '=op__orcamento', '=op__op', '=op__quant', 'op__cliente', 'op__servico', '=op__vendedor', ]
