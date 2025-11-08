from django.urls import reverse
from django.test import override_settings
from rest_framework.test import APITestCase

import json
from datetime import datetime
from urllib.parse import urlencode

from sponsors.models import Sponsorship


@override_settings(
    KOFI_VERIFICATION_TOKEN='valid-token'
)
class KofiTests(APITestCase):
    def setUp(self):
        self.TIMESTAMP = "2025-11-07T18:57:57Z"
        self.SINGLE_DONATION = {
            "verification_token": "valid-token",
            "message_id": "12345-67890",
            "timestamp": self.TIMESTAMP,
            "is_public": True,
            "from_name": "Jo Example",
            "message": "Good luck with the integration!",
            "amount": "3.00",
            "currency": "USD",
            "kofi_transaction_id": "00000000-1111-2222-3333-444444444444"
        }

        self.url = reverse('sponsors:kofi')

    def test_single_donation_success(self):
        resp = self.client.post(
            self.url,
            urlencode({'data': json.dumps(self.SINGLE_DONATION)}),
            content_type='application/x-www-form-urlencoded',
        )

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(Sponsorship.objects.count(), 1)
        self.assertEqual(
            Sponsorship.objects.first().start_date,
            datetime.fromisoformat(self.TIMESTAMP.replace('Z', '+00:00'))
        )

    def test_single_donation_success_null_message(self):
        data = self.SINGLE_DONATION.copy()
        data['message'] = None
        resp = self.client.post(
            self.url,
            urlencode({'data': json.dumps(data)}),
            content_type='application/x-www-form-urlencoded',
        )

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(Sponsorship.objects.count(), 1)

    def test_single_donation_bad_token(self):
        with self.assertLogs('django'):
            resp = self.client.post(
                self.url,
                urlencode({'data': json.dumps({'verification_token': 'bad-token'})}),
                content_type='application/x-www-form-urlencoded',
            )

        self.assertEqual(resp.status_code, 401)

    def test_single_donation_bad_content_type(self):
        with self.assertLogs('django'):
            resp = self.client.post(
                self.url,
                json.dumps(self.SINGLE_DONATION),
                content_type='application/json',
            )

        self.assertEqual(resp.status_code, 400)
