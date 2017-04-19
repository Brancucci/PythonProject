from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from operator import add, sub, mul, truediv
from fractions import Fraction
from django.contrib import messages
from .models import Results
from random import randint
from mathgame.forms import QuizzerForm


# Create your views here.

Users = Results.objects.all()


# def index(request):
#     return render(request, 'mathisfun/login.html')


def login_view(request):
    """ Login authentication for user

    Keyword requests:
    username -- POST parameter for username
    password -- POST parameter for user's password

    Returns: HttpResponse OR redirect
    upon success -- redirects user to 'Selection'
    Invalid username -- promts user that they do not exist
    Invalid password -- promts user that the password is incorrect

    """
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
    """ Main page for user that allows user to select activity for redirection"""
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
    ''' Handles the request for the solver functionality
    
    Args:
        request: the http request object
    Returns:
        rendering of the mathisfun/solver.html file    
    
    '''
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
    ''' Handles the request for the quizzing functionality
    
    Args:
        request: the http request object
    Returns:
        rendering of the mathisfun/quizzer.html file
        HttpResponseReidrect
    '''
    model = Results()
    if request.method == 'POST':
        form = QuizzerForm(request.POST)
        ops = {model.ADD: add, model.SUB: sub, model.MUL: mul, model.DIV: truediv}
        if form.is_valid():
            if form.cleaned_data.get('denominator') != 0:
                fraction1 = Fraction(int(request.POST['fraction1num']), int(request.POST['fraction1den']))
                fraction2 = Fraction(int(request.POST['fraction2num']), int(request.POST['fraction2den']))
                answer = ops[int(request.POST['operator'])](fraction1, fraction2)
                userAnswer = Fraction(form.cleaned_data.get('numerator'), form.cleaned_data.get('denominator'))
                if form.cleaned_data.get('numerator') == answer.numerator and form.cleaned_data.get('denominator') == answer.denominator:
                    average = 1
                    messages.success(request, '<div style="font-size: 20px;">Nice work! The answer you provided was correct<br/><strong>Grade Received: </strong>100%<br/><strong>Your Answer: </strong>' + str(userAnswer.numerator) + '/' + str(userAnswer.denominator) + '</div>', extra_tags='safe')
                elif userAnswer == answer:
                    average = .5
                    messages.warning(request, '<div style="font-size: 20px;">The answer you provided was correct but not reduced<br/><strong>Grade Received: </strong>50%<br/><strong>Your Answer: </strong>' + str(form.cleaned_data.get('numerator')) + '/' + str(form.cleaned_data.get('denominator')) + '<br/><strong>Correct Answer: </strong>' + str(answer.numerator) + '/' + str(answer.denominator) + '</div>', extra_tags='safe')
                else:
                    average = 0
                    messages.error(request, '<div style="font-size: 20px;">The answer you provided was not correct<br/><strong>Grade Received: </strong>0%<br/><strong>Your Answer: </strong>' + str(userAnswer.numerator) + '/' + str(userAnswer.denominator) + '<br/><strong>Correct Answer: </strong>' + str(answer.numerator) + '/' + str(answer.denominator) + '</div>', extra_tags='safe')
                model.userName = request.user.username
                model.operator = int(request.POST['operator'])
                model.average = average
                model.save()
            else:
                messages.error(request, '<div style="font-size: 20px;">Your answer cannot have a denominator with the value 0</div>', extra_tags='safe')
            return HttpResponseRedirect('/math/selection/quizzer')
    form = QuizzerForm()
    fraction1 = Fraction(randint(1,20), randint(1,20))
    fraction2 = Fraction(randint(1,20), randint(1,20))
    context = {'model': model, 'fraction1': fraction1, 'fraction2': fraction2, 'form': form}
    return render(request, 'mathisfun/quizzer.html', context)

@login_required
def results(request):
    return render(request, 'mathisfun/charts.html', {})



class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, user_id):
        data = {}

        currentUser = user_id
        sumScores = [[], [], [], []]
        averageScores = [None] * 5

        for score in Results.objects.filter(userName=currentUser):
            sumScores[score.operator].append(score.average)
        for s in sumScores:
            if len(s) > 0:
                averageScores[sumScores.index(s)] = (sum(s) / float(len(s)))
        total = []
        for i in range(4):
            if averageScores[i] is not None:
                total.append(averageScores[i])
            else:
                averageScores[i] = 0
        if len(total) > 0:
            averageScores[4] = sum(total) / float(len(total))
        else:
            averageScores[4] = 0
        for i in range(5):
            averageScores[i] = round(averageScores[i], 2)

        data.setdefault(currentUser, averageScores)
        data.setdefault("user", currentUser)

        allAverages = [[], [], [], [], []]
        for user in User.objects.all():
            sumScores = [[], [], [], []]
            averageScores = [None] * 5
            total.clear()

            for score in Results.objects.filter(userName=user):
                sumScores[score.operator].append(score.average)
            for s in sumScores:
                if len(s) > 0:
                    averageScores[sumScores.index(s)] = (sum(s) / float(len(s)))
            total = []
            for i in range(4):
                if averageScores[i] is not None:
                    total.append(averageScores[i])
            if len(total) > 0:
                averageScores[4] = sum(total) / float(len(total))
            else:
                averageScores[4] = None
            for i in range(5):
                if averageScores[i] is not None:
                    allAverages[i].append(averageScores[i])

        averageScores = [None] * 5
        for i in range(5):
            if len(allAverages[i]) > 0:
                averageScores[i] = sum(allAverages[i]) / float(len(allAverages[i]))
            else:
                averageScores[i] = 0
        for i in range(5):
            averageScores[i] = round(averageScores[i], 2)

        data.setdefault("all", averageScores)
        return Response(data)

