from django.forms import ModelForm, Form, TextInput, DateInput, NumberInput, TimeInput
from .models import *
from django.contrib import auth
from datetime import datetime

TIME_FORMAT = '%Y-%m-%d'

class ClientForm(ModelForm):
    class Meta():
        model = Client
        fields = ['name', 'sorname', 'number', 'birthday']
        widgets = {
            "name" : TextInput(attrs={"class" : "input", 'id' : 'input', 'name' : 'name', 'placeholder' : 'Имя'}),
            "sorname": TextInput(attrs={"class": "input", 'id': 'input', 'name' : 'sorname', 'placeholder' : 'Фамилия'}),
            "number": TextInput(attrs={"class": "phone", 'id': 'input', 'name' : 'number', 'placeholder' : '380(..)...-..-..'}),
            "birthday": DateInput(attrs={"class": "input", 'id': 'input', 'type' : 'date', 'min' : '1950-01-01', 'max' : '2000-12-31', 'name' : 'birthday', 'placeholder' : 'День рождения'}),
        }

class ServiceForm(ModelForm):
    class Meta():
        model = UslugaDlaClienta
        fields = ['date', 'time', 'cash', 'income', 'medicine', 'info']
        widgets = {
            "date": DateInput(attrs={"class": "input", 'id': 'input', 'type' : 'date', 'min' : datetime.today().strftime(TIME_FORMAT)}),
            "time": TimeInput(attrs={"class": "input", 'id': 'input', 'type' : 'time'}),
            "cash": NumberInput(attrs={"class": "input", 'id': 'input', 'placeholder' : 'Стоимость'}),
            "income": NumberInput(attrs={"class": "input", 'id': 'input', 'placeholder' : 'Прибыль'}),
            "medicine": TextInput(attrs={'class': 'input', 'id': 'input', 'placeholder' : 'Не обязательно'}),
            "info": TextInput(attrs={'class': 'input', 'id': 'input', 'placeholder': 'Не обязательно'})
        }

class CreateNewServiceForm(ModelForm):
    class Meta():
        model = Usluga
        fields = ['title']
        widgets = {
            "title" : TextInput(attrs={"class" : "input", 'id' : 'input', 'maxlength' : '30', 'placeholder' : 'Название процедуры'}),
        }

class EditClientForm(ModelForm):
    class Meta():
        model = Client
        fields = ['name', 'sorname', 'number', 'birthday', 'info']
        widgets = {
            "name" : TextInput(attrs={"class" : "input", 'id' : 'input'}),
            "sorname": TextInput(attrs={"class": "input", 'id': 'input'}),
            "number": NumberInput(attrs={"class": "number", 'id': 'input', 'type' : 'text', 'maxlength' : '12'}),
            "birthday": DateInput(attrs={"class": "input", 'id': 'input', 'type' : 'date', 'min' : '1950-01-01', 'max' : '2000-12-31'}),
            "info" : TextInput(attrs={'class' : 'input', 'id' : 'input', 'type' : 'text', 'maxlength' : '100'}),
        }


