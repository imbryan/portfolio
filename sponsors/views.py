from django.conf import settings
from django.shortcuts import render
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import json
import logging

from .models import Sponsorship
from .serializers import KofiSponsorSerializer

logger = logging.getLogger(__name__)

def index(request):
    sponsors = Sponsorship.objects.filter(hidden=False, expiration_date__gt=timezone.now()).order_by('-start_date')

    context = {
        'sponsors': sponsors,
    }
    return render(request, 'sponsors/index.html', context=context)

@api_view(['POST'])
def kofi(request):
    if request.META.get('CONTENT_TYPE') != 'application/x-www-form-urlencoded':
        return Response(status=status.HTTP_400_BAD_REQUEST)
    try:
        kofi_data = json.loads(request.data.get('data'))
    except Exception as e:
        logger.error(e)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if kofi_data.get('verification_token') != getattr(settings, 'KOFI_VERIFICATION_TOKEN', None):
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    serializer = KofiSponsorSerializer(data=kofi_data)
    if serializer.is_valid():
        serializer.save(
            platform='kofi',
            raw_payload=kofi_data,
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
    logger.error("Error: %s\nData: %s", serializer.errors, kofi_data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
