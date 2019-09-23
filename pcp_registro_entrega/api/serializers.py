from rest_framework.serializers import ModelSerializer
from pcp_registro_entrega.models import RegistroEntrega
from pcp_registro_op.api.serializers import RegistroOpSerializer


class RegistroEntregaSerializer(ModelSerializer):
    op = RegistroOpSerializer()

    class Meta:
        model = RegistroEntrega
        fields = [
            'id', 'op', 'produzido', 'obs',
            'prev_entrega', 'entrega', 'cancelada',
            'status', 'statusent',
        ]
