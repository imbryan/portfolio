from django.urls import path, re_path

from . import views

app_name = 'sponsors'

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^webhooks/kofi$', views.kofi, name='kofi'),
]
