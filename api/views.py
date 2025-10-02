from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404

from home.models import Project
from .serializers import ProjectSerializer

@api_view(['GET'])
def get_project(request, id):
    project = Project.objects.filter(id=id, hidden=False).first()
    if not project:
        raise NotFound()
    serializer = ProjectSerializer(project)
    return Response(serializer.data, status=200)
