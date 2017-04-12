from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # this includes all of the built in login, logout plus extra features
    url('^', include('django.contrib.auth.urls')),
    url(r'^login/mathisfun/selection/$', views.selection, name='selection'),
    url(r'^login/mathisfun/selection/quizzer/$', views.quizzer, name='quizzer'),
    url(r'^login/mathisfun/selection/solver/$', views.solver, name='solver'),
    url(r'^login/mathisfun/selection/results/$', views.results, name='results'),
    url(r'^results/api/chart/data/$', views.ChartData.as_view()),
]


# TODO remove these. they are for example purposes only
# # ex: /polls/
# url(r'^$', views.index, name='index'),
# # ex: /polls/5/
# url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
# # ex: /polls/5/results/
# url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
# # ex: /polls/5/vote/
# url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),