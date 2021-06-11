from . import views
from django.urls import path

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    # /polls/0/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # /polls/0/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    # /polls/0/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
