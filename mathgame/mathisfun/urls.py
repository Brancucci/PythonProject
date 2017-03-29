from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.selection, name='selection'),
    url(r'^quizzer/$', views.quizzer, name='quizzer'),
    url(r'^solver/$', views.solver, name='solver'),
    url(r'^results/$', views.results, name='results'),
    url(r'^login.html/$', views.login, name='login.html'),
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