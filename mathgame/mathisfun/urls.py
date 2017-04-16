from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # this includes all of the built in login and logout features
    url('^', include('django.contrib.auth.urls')),
    url(r'^selection/$', views.selection, name='selection'),
    url(r'^selection/quizzer/$', views.quizzer, name='quizzer'),
    url(r'^selection/solver/$', views.solver, name='solver'),
    url(r'^selection/results/$', views.results, name='results'),
    url(r'^selection/results/api/chart/data/$', views.ChartData.as_view()),
]
