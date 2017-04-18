from django import forms

class QuizzerForm(forms.Form):
    '''This form is a template for input validation on the Quizzer html form
    
    Args:
        forms.Form: djang.forms.Form
    '''
    numerator = forms.IntegerField(label="", required=True)
    denominator = forms.IntegerField(label="", required=True)
    operator = forms.IntegerField(widget=forms.HiddenInput(), required=True)