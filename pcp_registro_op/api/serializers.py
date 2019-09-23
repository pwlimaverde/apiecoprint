from rest_framework.serializers import ModelSerializer
from pcp_registro_op.models import RegistroOp


class RegistroOpSerializer(ModelSerializer):

    class Meta:
        model = RegistroOp
        fields = [
            'id', 'orcamento', 'cliente', 'servico',
            'quant', 'valor', 'entrada', 'vendedor',
            'op',
        ]
