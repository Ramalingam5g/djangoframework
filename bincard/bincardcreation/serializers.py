from rest_framework import serializers
from bincardcreation.models import material

class materialserializers(serializers.ModelSerializer):

    class Meta:
        model = material
        fields = '__all__'
        # fields =['date',
        # 'doc_no',
        # 'received_from',
        # 'receipt_no',
        # 'issue',
        # 'balance',
        # 'verification_date',
        # 'verified_by']