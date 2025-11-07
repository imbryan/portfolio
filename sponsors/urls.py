from django.urls import path

from . import views

app_name = 'sponsors'

urlpatterns = [
    path('', views.index, name='index'),
    path('webhooks/kofi/', views.kofi, name='kofi'),
]
