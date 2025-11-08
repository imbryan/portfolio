from constance import config
from rest_framework import serializers

from datetime import timedelta

from sponsors.models import Sponsorship


class KofiSponsorSerializer(serializers.ModelSerializer):
    """
    https://ko-fi.com/manage/webhooks
    """
    message_id = serializers.CharField(source='platform_message_id')
    kofi_transaction_id = serializers.CharField(source='platform_transaction_id')
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    currency = serializers.CharField()
    from_name = serializers.CharField(source='name')
    message = serializers.CharField(allow_null=True)
    is_public = serializers.BooleanField(source='is_message_public')
    timestamp = serializers.DateTimeField(source='start_date')

    class Meta:
        model = Sponsorship
        fields = [
            'message_id',
            'kofi_transaction_id',
            'amount',
            'currency',
            'from_name',
            'message',
            'is_public',
            'timestamp',
        ]
        
    def create(self, validated_data):
        start_date = validated_data.get('start_date')
        expiration_date = start_date + timedelta(days=getattr(config, 'SPONSOR_DURATION'))
        validated_data['expiration_date'] = expiration_date
        return super().create(validated_data)
