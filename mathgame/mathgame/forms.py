from django import forms

class QuizzerForm(forms.Form):
    numerator = forms.IntegerField(label="", min_value=1, required=True)
    denominator = forms.IntegerField(label="", min_value=1, required=True)