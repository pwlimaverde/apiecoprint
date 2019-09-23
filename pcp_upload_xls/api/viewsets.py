from datetime import datetime
import xlrd
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import (
    IsAuthenticated, IsAdminUser, DjangoModelPermissions,
    IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly
)
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from pcp_upload_xls.models import Upload_list_op
from pcp_registro_op.models import RegistroOp
from pcp_registro_entrega.models import RegistroEntrega
from .serializers import UploadListOpSerializer


class UploadListOpViewSet(ModelViewSet):

    queryset = Upload_list_op.objects.all().order_by('descricao')
    serializer_class = UploadListOpSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    filter_backends = (SearchFilter, )
    search_fields = ['descricao', ]


    def create(self, request, *args, **kwargs):

        context = {}

        xls_file = request.data['arquivo']

        if not xls_file.name.endswith('.xls'):
            return Response({'erro': 'o arquivo não é um xls'})

        Upload_list_op.objects.update_or_create(descricao=xls_file.name, arquivo=xls_file)
        caminho = 'static/arquivosxls/' + xls_file.name

        workbook = xlrd.open_workbook(caminho)
        worksheet = workbook.sheet_by_index(0)
        datemode = workbook.datemode

        listaxls = []

        for row_num in range(worksheet.nrows):
            row = worksheet.row_values(row_num)
            row[5] = datetime(*xlrd.xldate_as_tuple(row[5], datemode))
            row[8] = datetime(*xlrd.xldate_as_tuple(row[8], datemode))
            listaxls.append(row)

        for item in listaxls:
            try:
                RegistroOp.objects.update_or_create(
                    orcamento=item[0],
                    cliente=item[1],
                    servico=item[2],
                    quant=item[3],
                    valor=item[4],
                    entrada=item[5],
                    vendedor=item[6],
                    op=item[7],
                )

                cons = RegistroOp.objects.all().order_by("-id")[0]
                RegistroEntrega.objects.update_or_create(op=cons, prev_entrega=item[8])
            except:
                pass

        now = datetime.now().strftime("%d-%m-%y as %H:%M:%S")
        context['listaxls'] = listaxls

        return Response({'Status': 'Upload realizado com sucesso em: ' + str(now), 'Relação dos Upload:': context['listaxls']})
