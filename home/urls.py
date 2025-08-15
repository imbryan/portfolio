from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    #path('skills', views.SkillsView.as_view(), name='skills'),
    #path('contact', views.ContactView.as_view(), name='contact'),
    path('projects/', views.projects, name='projects'),
    # path('activism/', views.activism, name='activism'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:id>/', views.blog_post, name="blog_post_by_id"),
    path('blog/<slug:slug>/', views.blog_post, name="blog_post_by_slug"),
]
