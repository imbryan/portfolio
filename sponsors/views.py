from django.shortcuts import render
from django.utils import timezone

from .models import Sponsorship

def index(request):
    sponsors = Sponsorship.objects.filter(hidden=False, expiration_date__gt=timezone.now()).order_by('-start_date')

    context = {
        'sponsors': sponsors,
    }
    return render(request, 'sponsors/index.html', context=context)
