from django import forms
from django.forms import DateInput, DateField

class CalculateIntervalForm(forms.Form):
    date_from = forms.DateField(widget= DateInput(attrs={"class" : "input", 'id' : 'input', 'name' : 'date_from', 'type' : 'date'}), label=None)
    date_to = forms.DateField(widget= DateInput(attrs={"class" : "input", 'id' : 'input', 'name' : 'date_from', 'type' : 'date'}), label=None)
