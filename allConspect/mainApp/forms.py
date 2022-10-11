from django import forms
from .models import *

class AddFormulaForm(forms.Form):
    name = forms.CharField(max_length=50, label="Название")
    body = forms.CharField(max_length=1000, label="Формула")
    isLatex = forms.BooleanField(required=False)