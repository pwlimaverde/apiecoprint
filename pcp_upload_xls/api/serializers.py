from rest_framework.serializers import ModelSerializer
from pcp_upload_xls.models import Upload_list_op


class UploadListOpSerializer(ModelSerializer):

    class Meta:
        model = Upload_list_op
        fields = '__all__'
