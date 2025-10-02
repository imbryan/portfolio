from django.urls import path
from . import views

urlpatterns = [
    path('project/<int:id>/', views.get_project),
]