from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import (
    IsAuthenticated, IsAdminUser, DjangoModelPermissions,
    IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly
)
from rest_framework.viewsets import ModelViewSet
from pcp_upload_xls.models import Upload_list_op
from .serializers import UploadListOpSerializer


class UploadListOpViewSet(ModelViewSet):

    queryset = Upload_list_op.objects.all().order_by('descricao')
    serializer_class = UploadListOpSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    #filterset_fields = ('cliente', 'servico', 'quant')
    #filter_backends = (SearchFilter, )
    #search_fields = ['id', '=op__orcamento', '=op__op', '=op__quant', 'op__cliente', 'op__servico', '=op__vendedor', ]
