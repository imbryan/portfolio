from rest_framework import serializers

from home.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id',
            'project_title',
            'project_role',
            'project_body',
            'project_repository_url',
            'project_demo_url',
            'project_board_url',
            'project_download_url',
            'image_url',
            'date',
        ]