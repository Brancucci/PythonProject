from django.contrib.auth import login, authenticate
from django import forms
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from operator import add, sub, mul, truediv
from fractions import Fraction
from django.contrib import messages
from .models import Results
from random import randint
from mathgame.forms import QuizzerForm

# Create your views here.

Users = Results.objects.all()


def index(request):
    return render(request, 'mathisfun/login.html')


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('selection')
        else:
            pass
            return HttpResponse('<h1>User not active</h1>')
    else:
        return HttpResponse('<h1>User does not exist</h1>')


@login_required
def selection(request):
    return render(request, 'mathisfun/selection.html')

OP_CHOICES = (
        ('addition', '+'),
        ('subtraction', '-'),
        ('multiplication', '×'),
        ('division', '÷'),
    )


class ChoiceForm(forms.Form):
    operations = forms.ChoiceField(choices=OP_CHOICES)


@login_required
def solver(request):
    """This function renders the Fraction Solver to help users with fractional math."""
    ops = {'addition': add,
           'subtraction': sub,
           'multiplication': mul,
           'division': truediv
           }
    opdropdown = ChoiceForm()
    context = {'myoperators': opdropdown}
    getrequest = request.GET
    # This covers the case when the user first loads the Solver page
    if len(getrequest) == 0:
        return render(request, 'mathisfun/solver.html', context)
    try:
        for x in getrequest.keys():
            if not getrequest[x]:
                # Missing input, prompt user to enter all values
                raise ValueError
        op = getrequest.get('operations', None)
        leftfract = Fraction(int(getrequest.get('left_num', None)), int(getrequest.get('left_denom', None)))
        rightfract = Fraction(int(getrequest.get('right_num', None)), int(getrequest.get('right_denom', None)))
        resultfract = ops[op](leftfract, rightfract)
        opdropdown.fields['operations'].initial = op
        context = {'result_num': resultfract.numerator, 'result_denom': resultfract.denominator,
                   'left_num': leftfract.numerator, 'left_denom': leftfract.denominator,
                   'right_num': rightfract.numerator, 'right_denom': rightfract.denominator,
                   'myoperators': opdropdown}
        # This covers the standard case when the user entered all faction values and submits to see the results
        return render(request, 'mathisfun/solver.html', context)
    except ValueError:
        """This covers the case when the user hasn't entered all values"""
        messages.error(request, 'You must enter all fraction values!')
        return render(request, 'mathisfun/solver.html', context)
    except ZeroDivisionError:
        """This covers the case when the denominator is zero, Fraction throws a ZeroDivisionError"""
        messages.error(request, 'Denominators cannot be zero!')
        return render(request, 'mathisfun/solver.html', context)


@login_required
def quizzer(request):
    if request.method == 'POST':
        form = QuizzerForm(request.POST)
        ops = {Results.ADD: add, Results.SUB: sub, Results.MUL: mul, Results.DIV: truediv}
        if form.is_valid():
            fraction1 = Fraction(int(request.POST['fraction1num']), int(request.POST['fraction1den']))
            fraction2 = Fraction(int(request.POST['fraction2num']), int(request.POST['fraction2den']))
            answer = ops[int(request.POST['operator'])](fraction1, fraction2)
            userAnswer = Fraction(form.cleaned_data.get('numerator'), form.cleaned_data.get('denominator'))
            if form.cleaned_data.get('numerator') == answer.numerator and form.cleaned_data.get('denominator') == answer.denominator:
                return HttpResponse("100%")
            elif userAnswer == answer:
                return HttpResponse("50%")
            else:
                return HttpResponse("0%")
    else:
        model = Results()
        fraction1 = Fraction(randint(1,20), randint(1,20))
        fraction2 = Fraction(randint(1,20), randint(1,20))
        form = QuizzerForm()
        context = {'model': model, 'fraction1': fraction1, 'fraction2': fraction2, 'form': form}
        return render(request, 'mathisfun/quizzer.html', context)

@login_required
def results(request):
    return render(request, 'mathisfun/charts.html', {})


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = {}
        # ***************************************************************
        # This needs to be replaced for the user that is logged in
        currentUser = "<userid>"
        data.setdefault(currentUser, [5, 4, 6, 5, 20])
        # ***************************************************************
        data.setdefault("user", currentUser)
        sumScores = [0, 0, 0, 0, 0]
        for user in Results.objects.all():
            sumScores[0] = sumScores[0] + user.addition
            sumScores[1] = sumScores[1] + user.subtraction
            sumScores[2] = sumScores[2] + user.multiplication
            sumScores[3] = sumScores[3] + user.division
            sumScores[4] = sumScores[4] + user.total
        count = Users.count()

        averageScores = [
            sumScores[0] / count,
            sumScores[1] / count,
            sumScores[2] / count,
            sumScores[3] / count,
            sumScores[4] / count
        ]
        data.setdefault("all", averageScores)
        return Response(data)

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
