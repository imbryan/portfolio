from rest_framework.test import APITestCase

from home.models import Project


class ProjectTests(APITestCase):
    def setUp(self):
        Project.objects.create(
            id=1,
            project_title="Project",
            project_body="Visible project",
        )
        Project.objects.create(
            id=2,
            project_title="Hidden project",
            project_body="You can't see me",
            hidden=True,
        )

    def test_get_project_ok(self):
        resp = self.client.get('/api/project/1/')
        self.assertEqual(resp.data['id'], 1)
        self.assertEqual(resp.status_code, 200)

    def test_get_project_not_found(self):
        resp = self.client.get('/api/project/2/')
        self.assertEqual(resp.status_code, 404)
