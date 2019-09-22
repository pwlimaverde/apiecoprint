from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import (
    IsAuthenticated, IsAdminUser, DjangoModelPermissions,
    IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly
)
from rest_framework.viewsets import ModelViewSet
from pcp_registro_op.models import RegistroOp
from .serializers import RegistroOpSerializer


class RegistroOpViewSet(ModelViewSet):

    queryset = RegistroOp.objects.all().order_by('-op')
    serializer_class = RegistroOpSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    #filterset_fields = ('cliente', 'servico', 'quant')
    filter_backends = (SearchFilter, )
    search_fields = ['=id', '=orcamento', '=op', '=quant', 'cliente', 'servico', '=vendedor', ]
