from django.shortcuts import render, redirect
from django.contrib import auth
from MedApp.models import *
from datetime import datetime

# Create your views here.

TIME_FORMAT = '%Y-%m-%d'
DAYS = {
        'Monday' : 'Понедельник',
        'Tuesday' : 'Вторник',
        'Wednesday' : 'Среда',
        'Thursday' : 'Четверг',
        'Friday' : 'Пятница',
        'Saturday' : 'Суббота',
        'Sunday' : 'Воскресенье',
        }

def journal(request):
    if auth.get_user(request).is_active:
        out_dict = {}
        today = datetime.today().date()
        out_dict['journalapp_active'] = True
        out_dict['User'] = auth.get_user(request)
        out_dict['Clients'] = Client.objects.filter(user_id = auth.get_user(request).id)
        out_dict['ServicesForClients'] = UslugaDlaClienta.objects.filter(user_id = auth.get_user(request).id)
        out_dict['Services'] = Usluga.objects.all()
        out_dict['Today'] = datetime.today().date()
        dates = []
        days_ru = []
        for date in UslugaDlaClienta.objects.filter(user_id = auth.get_user(request).id).order_by('date'):
            if date.date not in dates:
                dates.append(date.date)
        out_dict['Dates'] = dates
        for day in dates:
            if day >= today:
                day_eng = day.strftime('%A')
                day_str = DAYS.get(day_eng)
                days_ru.append(day_str)
        out_dict['DaysRu'] = days_ru
        return render(request, 'journal/journal.html', out_dict)
    else:
        return redirect('/')

def calculate(request, date):
    return redirect('/calculate/')