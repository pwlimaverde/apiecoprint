from datetime import datetime
# from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import (
    IsAuthenticated, IsAdminUser, DjangoModelPermissions,
    IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly
)
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from pcp_registro_entrega.models import RegistroEntrega
from .serializers import RegistroEntregaSerializer


class RegistroEntregaViewSet(ModelViewSet):

    queryset = RegistroEntrega.objects.all().order_by('prev_entrega')
    serializer_class = RegistroEntregaSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    #filterset_fields = ('cliente', 'servico', 'quant')
    filter_backends = (SearchFilter, )
    search_fields = ['id', '=op__orcamento', '=op__op', '=op__quant', 'op__cliente', 'op__servico', '=op__vendedor', ]

    @action(methods=['patch'], detail=True)
    def upprod(self, request, pk=None):
        ent = datetime.now()
        RegistroEntrega.objects.filter(pk=pk).update(produzido=ent)
        return Response({'Status': 'Produção da OP Registrada'})

    @action(methods=['patch'], detail=True)
    def upent(self, request, pk=None):
        ent = datetime.now()
        RegistroEntrega.objects.filter(pk=pk).update(entrega=ent)
        return Response({'Status': 'Entrega da OP Registrada'})

    @action(methods=['patch'], detail=True)
    def canprod(self, request, pk=None):
        RegistroEntrega.objects.filter(pk=pk).update(cancelada=True)
        return Response({'Status': 'OP Cancelada'})

    @action(methods=['patch'], detail=True)
    def atprod(self, request, pk=None):
        RegistroEntrega.objects.filter(pk=pk).update(cancelada=False)
        return Response({'Status': 'OP Ativada'})
