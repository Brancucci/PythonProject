from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def selection(request):

    return render(request, 'mathisfun/selection.html')

def solver(request):
    #return HttpResponse("Inside solver")
    return render(request, 'mathisfun/solver.html')

def quizzer(request):
    #return HttpResponse("Inside quizzer")
    return render(request, 'mathisfun/quizzer.html')

def results(request):
    return HttpResponse("inside results")


# TODO remove these. they are just for example purposes
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
#
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
#
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
