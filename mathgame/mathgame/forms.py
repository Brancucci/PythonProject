from django import forms

class QuizzerForm(forms.Form):
    numerator = forms.IntegerField(label="", required=True)
    denominator = forms.IntegerField(label="", required=True)
    operator = forms.IntegerField(widget=forms.HiddenInput(), required=True)