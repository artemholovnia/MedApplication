from django.shortcuts import render, redirect
from django.contrib import auth
from datetime import datetime, timedelta, date
from MedApp.models import *
import calendar
from calculate.forms import CalculateIntervalForm
# Create your views here.

HOME_PATH = '/'
TIME_FORMAT = '%Y-%m-%d'
VALUE = (date.today() - timedelta(days = 30)).strftime(TIME_FORMAT)
MIN_DATE = date.today() - timedelta(days = 365)
MAX_DATE = date.today().strftime(TIME_FORMAT)

'''def name(request):
    if auth.get_user(request).is_active:
        out_dict = {}
        out_dict['User'] = auth.get_user(request)
    else:
        return redirect('/')'''

def name(request):
    if auth.get_user(request).is_active:
        out_dict = {}
        out_dict['calculateapp_active'] = True
        out_dict['User'] = auth.get_user(request)
        out_dict['Today'] = date.today().strftime(TIME_FORMAT)
        out_dict['Yesterday'] = (date.today() - timedelta(days = 1)).strftime(TIME_FORMAT)
        return render(request, 'calculate/template.html', out_dict)
    else:
        return redirect('/')

def calculate_menu(request):
    if auth.get_user(request).is_active:
        out_dict = {}
        out_dict['calculateapp_active'] = True
        out_dict['User'] = auth.get_user(request)
        return render(request, 'calculate/calculate-menu.html', out_dict)
    else:
        return redirect('/')

def calculate_today(request):
    if auth.get_user(request).is_active:
        out_dict = {}
        out_dict['calculateapp_active'] = True
        out_dict['User'] = auth.get_user(request)
        today = date.today()
        today_str = today.strftime(TIME_FORMAT)
        yesterday = today - timedelta(days = 0)
        count_days = (today - yesterday).days + 1
        cash = 0
        days = []
        income = 0
        for itteration in range(0, count_days):
            date_day = yesterday + timedelta(days = itteration)
            days.append(date_day)
            for service in UslugaDlaClienta.objects.filter(user_id = auth.get_user(request).id):
                if date_day == service.date:
                    cash += service.cash
                    income += service.income
        out_dict['ServicesForClients'] = UslugaDlaClienta.objects.filter(user_id = auth.get_user(request).id)
        out_dict['Clients'] = Client.objects.filter(user_id=auth.get_user(request).id)
        out_dict['Services'] = Usluga.objects.all()
        out_dict['Days'] = days
        out_dict['Cash'] = cash
        out_dict['Income'] = income
        out_dict['Date'] = today_str
        return render(request, 'calculate/test.html', out_dict)
    else:
        return redirect('/')

def calculate_yesterday(request):
    if auth.get_user(request).is_active:
        out_dict = {}
        out_dict['calculateapp_active'] = True
        out_dict['User'] = auth.get_user(request)
        today = date.today()
        yesterday = today - timedelta(days = 1)
        count_days = (today - yesterday).days
        yesterday_str = yesterday.strftime(TIME_FORMAT)
        days = []
        cash = 0
        income = 0
        for itteration in range(0, count_days):
            date_day = yesterday + timedelta(days = itteration)
            days.append(date_day)
            for service in UslugaDlaClienta.objects.filter(user_id = auth.get_user(request).id):
                if date_day == service.date:
                    cash += service.cash
                    income += service.income
        out_dict['ServicesForClients'] = UslugaDlaClienta.objects.filter(user_id = auth.get_user(request).id)
        out_dict['Clients'] = Client.objects.filter(user_id=auth.get_user(request).id)
        out_dict['Services'] = Usluga.objects.all()
        out_dict['Days'] = days
        out_dict['Cash'] = cash
        out_dict['Income'] = income
        out_dict['Date'] = yesterday_str
        return render(request, 'calculate/test.html', out_dict)
    else:
        return redirect('/')

def calculate_week(request):
    if auth.get_user(request).is_active:
        out_dict = {}
        out_dict['calculateapp_active'] = True
        out_dict['User'] = auth.get_user(request)
        today = date.today()
        date_to_str = today.strftime(TIME_FORMAT)
        date_from = today - timedelta(days = 6)
        date_from_str = date_from.strftime(TIME_FORMAT)
        count_days = (today - date_from).days + 1
        cash = 0
        days = []
        income = 0
        for itteration in range(0, count_days):
            date_day = date_from + timedelta(days = itteration)
            days.append(date_day)
            for service in UslugaDlaClienta.objects.filter(user_id = auth.get_user(request).id):
                if date_day == service.date:
                    cash += service.cash
                    income += service.income
        out_dict['ServicesForClients'] = UslugaDlaClienta.objects.filter(user_id = auth.get_user(request).id)
        out_dict['Clients'] = Client.objects.filter(user_id=auth.get_user(request).id)
        out_dict['Services'] = Usluga.objects.all()
        out_dict['Days'] = days
        out_dict['Cash'] = cash
        out_dict['Income'] = income
        out_dict['DateFrom'] = date_from_str
        out_dict['DateTo'] = date_to_str
        return render(request, 'calculate/test.html', out_dict)
    else:
        return redirect('/')

def calculate_month(request):
    if auth.get_user(request).is_active:
        out_dict = {}
        out_dict['calculateapp_active'] = True
        out_dict['User'] = auth.get_user(request)
        #Сегодняшняя дата
        today = date.today()
        date_to_str = today.strftime(TIME_FORMAT)
        #Вычисление для получения кол-ва дней в месяце
        edit_date_to = date_to_str.split('-')
        month = int(edit_date_to[1]) - 1
        if month < 10:
            month = '0' + str(month)
        else:
            month = str(month)
        date_from_str_month = edit_date_to[0] + '-' + month + '-' + edit_date_to[2]
        date_from_month = datetime.strptime(date_from_str_month, TIME_FORMAT)
        count_days = calendar.mdays[date_from_month.month] + 1
        #Дата начала отсчета
        date_from = today - timedelta(days = count_days - 1)
        date_from_str = date_from.strftime(TIME_FORMAT)
        cash = 0
        days = []
        income = 0
        for itteration in range(0, count_days):
            date_day = date_from + timedelta(days = itteration)
            days.append(date_day)
            for service in UslugaDlaClienta.objects.filter(user_id = auth.get_user(request).id):
                if date_day == service.date:
                    cash += service.cash
                    income += service.income
        out_dict['ServicesForClients'] = UslugaDlaClienta.objects.filter(user_id = auth.get_user(request).id)
        out_dict['Clients'] = Client.objects.filter(user_id=auth.get_user(request).id)
        out_dict['Services'] = Usluga.objects.all()
        out_dict['Days'] = days
        out_dict['Cash'] = cash
        out_dict['Income'] = income
        out_dict['DateFrom'] = date_from_str
        out_dict['DateTo'] = date_to_str
        return render(request, 'calculate/test.html', out_dict)
    else:
        return redirect('/')

def interval(request):
    if auth.get_user(request).is_active:
        out_dict = {}
        out_dict['calculateapp_active'] = True
        out_dict['User'] = auth.get_user(request)
        out_dict['MaxDate'] = MAX_DATE
        out_dict['MinDate'] = MIN_DATE
        out_dict['Value'] = date.today().strftime(TIME_FORMAT)
        if request.method == 'POST':
            #test
            DATE = datetime.strptime(request.POST.get('date_from', ''), TIME_FORMAT)
            TESTING_DATE = datetime.date(DATE)
            # Сегодняшняя дата
            date_to = datetime.strptime(request.POST.get('date_to', ''), TIME_FORMAT)
            date_to_str = date_to.strftime(TIME_FORMAT)
            # Дата начала отсчета
            date_from = datetime.strptime(request.POST.get('date_from', ''), TIME_FORMAT)
            date_from_str = date_from.strftime(TIME_FORMAT)
            count_days = (date_to - date_from).days + 1
            cash = 0
            days = []
            income = 0
            for itteration in range(0, count_days):
                date_day = datetime.date(date_from + timedelta(days=itteration))
                days.append(date_day)
                for service in UslugaDlaClienta.objects.filter(user_id = auth.get_user(request).id):
                    if date_day == service.date:
                        cash += service.cash
                        income += service.income
            out_dict['ServicesForClients'] = UslugaDlaClienta.objects.filter(user_id = auth.get_user(request).id)
            out_dict['Clients'] = Client.objects.filter(user_id=auth.get_user(request).id)
            out_dict['Services'] = Usluga.objects.all()
            out_dict['Days'] = days
            out_dict['Cash'] = cash
            out_dict['Income'] = income
            out_dict['DateFrom'] = date_from_str
            out_dict['DateTo'] = date_to_str
            return render(request, 'calculate/test.html', out_dict)
        else:
            out_dict['form'] = CalculateIntervalForm()
        return render(request, 'calculate/calculate-interval.html', out_dict)
    else:
        return redirect('/')

def calculate_date(request, date):
    if auth.get_user(request).is_active:
        user = auth.get_user(request).id
        out_dict = {}
        out_dict['calculateapp_active'] = True
        out_dict['User'] = auth.get_user(request)
        date_str = date[:-1].split('_')
        date_strptime_str = date_str[2] + '-' + date_str[1] + '-' + date_str[0]
        date = datetime.strptime(date_strptime_str, TIME_FORMAT).date()
        days = []
        days.append(date)
        cash = 0
        income = 0
        for service in UslugaDlaClienta.objects.filter(user_id = auth.get_user(request).id):
            if date == service.date:
                cash += service.cash
                income += service.income
        out_dict['ServicesForClients'] = UslugaDlaClienta.objects.filter(date = date).filter(user_id = auth.get_user(request).id)
        out_dict['Clients'] = Client.objects.filter(user_id = user)
        out_dict['Services'] = Usluga.objects.all()
        out_dict['Days'] = days
        out_dict['Cash'] = cash
        out_dict['Income'] = income
        out_dict['Date'] = date.strftime(TIME_FORMAT)
        return render(request, 'calculate/test.html', out_dict)
    else:
        return redirect('/')