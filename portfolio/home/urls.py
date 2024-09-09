from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('old/', views.index, name='index'),
    #path('skills', views.SkillsView.as_view(), name='skills'),
    #path('contact', views.ContactView.as_view(), name='contact'),
    #path('projects', views.ProjectsView.as_view(), name='projects'),
    path('old/blog', views.blog, name='blog')
]