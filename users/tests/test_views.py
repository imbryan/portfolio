from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from unittest.mock import patch, Mock

class LoginTestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.username = 'tester'
        self.password = 'password'
        self.user = User.objects.create_user(username=self.username, password=self.password)


        self.mock_successful_turnstile_response = Mock(status_code=200)
        self.mock_successful_turnstile_response.json.return_value = {'success': True}

        self.mock_failed_turnstile_response = Mock()
        self.mock_failed_turnstile_response.json.return_value = {'success': False, 'error-codes': {'internal-error'}}

    @patch('requests.post')
    @patch('core.utils.turnstile_utils.validate_turnstile')
    def test_login_successful_htmx(self, mock_validate_turnstile, mock_requests_post):
        mock_requests_post.return_value = self.mock_successful_turnstile_response
        mock_validate_turnstile.return_value = self.mock_successful_turnstile_response

        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': self.password,
            'cf-turnstile-response': 'valid-token',
        }, headers={'HX-Request': 'true'})

        self.assertIn('HX-Redirect', response.headers)
        self.assertEqual(response.status_code, 200)

    @patch('requests.post')
    @patch('core.utils.turnstile_utils.validate_turnstile')
    def test_login_successful(self, mock_validate_turnstile, mock_requests_post):
        mock_requests_post.return_value = self.mock_successful_turnstile_response
        mock_validate_turnstile.return_value = self.mock_successful_turnstile_response

        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': self.password,
            'cf-turnstile-response': 'valid-token',
        }, follow=False)

        self.assertNotIn('HX-Redirect', response.headers)
        self.assertEqual(response.status_code, 302)

    @patch('requests.post')
    @patch('core.utils.turnstile_utils.validate_turnstile')
    def test_login_failed_turnstile_invalid(self, mock_validate_turnstile, mock_requests_post):
        mock_requests_post.return_value = self.mock_failed_turnstile_response
        mock_validate_turnstile.return_value = self.mock_failed_turnstile_response

        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': self.password,
            'cf-turnstile-response': 'invalid-token',
        })

        self.assertNotIn('HX-Redirect', response.headers)
        self.assertEqual(response.status_code, 200)

    @patch('requests.post')
    @patch('core.utils.turnstile_utils.validate_turnstile')
    def test_login_failed_credentials_invalid(self, mock_validate_turnstile, mock_requests_post):
        mock_requests_post.return_value = self.mock_successful_turnstile_response
        mock_validate_turnstile.return_value = self.mock_successful_turnstile_response

        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': 'wrong',
            'cf-turnstile-response': 'valid-token',
        })

        self.assertNotIn('HX-Redirect', response.headers)
        self.assertEqual(response.status_code, 200)
