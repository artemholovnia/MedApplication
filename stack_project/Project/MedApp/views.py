from django.shortcuts import render, redirect
from django.template import loader, RequestContext, Context
from django.template.loader import render_to_string
from django.contrib import auth
from datetime import datetime
from django.http import JsonResponse
from .forms import *
from .context_processor import *
import string
import random

LENGTH_NUMBER = 12
LENGTH_NAME = 20
LENGTH_SORNAME = 20
LENGTH_INFO = 100
MAX_DATE = datetime.strptime('2000-12-31', '%Y-%m-%d')
MIN_DATE = datetime.strptime('1950-01-01', '%Y-%m-%d')
MIN_DATE_STR = '1950-01-01'
MAX_DATE_STR = '2000-12-31'
TIME_FORMAT = '%Y-%m-%d'


#Phone number validation(start)
def phone_validation(phone_number):
    if phone_number[0] == '3':
        phone_number = '+' + phone_number
    elif phone_number[0] == '0':
        phone_number = '+38' + phone_number
    else:
        return 'Validation Error'
    valid_phone = phone_number[0:4] + '(' + phone_number[4:6] + ')-' + phone_number[6:9] + '-' + phone_number[9:11] + '-' + phone_number[11:13]
    return str(valid_phone)
#(end)

#Home page(start)
def home(request):
    out_dict = {}
    out_dict['medapp_active'] = True
    return render(request, 'MedApp/template.html', out_dict)
#(end)

#Page all clients(start)
def clients(request):
    if auth.get_user(request).is_active:
        out_dict = {}
        out_dict['medapp_active'] = True
        out_dict['Clients'] = Client.objects.filter(user_id = auth.get_user(request).id)
        error_message = 'Клиент не найден. Попробуйте еще раз или '
        error_message_none = 'Заполните поля для поиска'

        clients = Client.objects.filter(user_id = auth.get_user(request).id)
        if request.method == 'POST':
            search_text = request.POST.get('find_client', '')
            if search_text != '':
                first_symbol = search_text[0].upper()
                search_text = first_symbol + search_text[1:]
                find_clients = clients.filter(name = search_text)
                if find_clients:
                    out_dict['Clients'] = find_clients
                    return render(request, 'MedApp/client_base.html', out_dict)
                else:
                    find_clients = clients.filter(sorname = search_text)
                    if find_clients:
                        out_dict['Clients'] = find_clients
                        return render(request, 'MedApp/client_base.html', out_dict)
                    else:
                        if search_text[0] == '+':
                            phone_number = search_text[0:4] + '(' + search_text[4:6] + ')-' + search_text[6:9] + '-' + search_text[9:11] + '-' + search_text[11:13]
                            find_clients = clients.filter(number = phone_number)
                            if find_clients:
                                out_dict['Clients'] = find_clients
                                return render(request, 'MedApp/client_base.html', out_dict)
                            else:
                                out_dict['ErrorMessage'] = error_message
                        else:
                            out_dict['ErrorMessage'] = error_message
                            return render(request, 'MedApp/client_base.html', out_dict)
            else:
                out_dict['ErrorMessage'] = 'ПУсто'
                return redirect('/')
    return render(request, 'MedApp/client_base.html', out_dict)
#(end)

#Page one client info(start)
def client_info(request, client_token):
    if auth.get_user(request).is_active:
        out_dict = {}
        out_dict['medapp_active'] = True
        user_validation = False
        if auth.get_user(request).id == Client.objects.get(token=client_token).user_id:
            sum_income = 0
            sum_cash = 0
            client_id = Client.objects.get(token=client_token).id
            services = UslugaDlaClienta.objects.filter(foreign_key_id=client_id)
            for income in services:
                sum_income += income.income
            for cash in services:
                sum_cash += cash.cash
            out_dict['ServicesList'] = Usluga.objects.all()
            out_dict['Client'] = Client.objects.get(token=client_token)
            out_dict['BirthdayStr'] = Client.objects.get(token=client_token).birthday
            out_dict['RegistrationDate'] = Client.objects.get(token = client_token).registration_date
            out_dict['Services'] = UslugaDlaClienta.objects.filter(foreign_key_id=client_id)
            out_dict['Income'] = sum_income
            out_dict['Cash'] = sum_cash
            return render(request, 'MedApp/client_info.html', out_dict)
        else:
            return redirect('/')
    else:
        return redirect('/')
#(end)

#Regstration new client(start)
def registration_client(request):
    if auth.get_user(request).is_active:
        url = '/medapp/clients/'
        out_dict = {}
        error_message = 'Введены не правильные данные'
        validation = True

        #Token
        token = []
        token_join = ''
        for x in range(32):
            sym = random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
            token.append(sym)
        token_str = token_join.join(token)

        out_dict['medapp_active'] = True
        out_dict['MinDate'] = MIN_DATE_STR
        out_dict['MaxDate'] = MAX_DATE_STR
        if request.method == 'POST':
            name = request.POST.get('name', '')
            sorname = request.POST.get('sorname', '')
            number = request.POST.get('number', '')
            form = ClientForm(request.POST)
            if form.is_valid():
                client = form.save(commit=False)
                #Name validation - TRUE
                if name != '':
                    if name.isalpha():
                        name_edit = name.lower()
                        name = name_edit[0].upper() + name_edit[1:]
                        client.name = name
                    else:
                        validation = False
                #Sorname validation - TRUE
                if sorname != '':
                    if sorname.isalpha():
                        sorname_edit = sorname.lower()
                        sorname = sorname_edit[0].upper() + sorname_edit[1:]
                        client.sorname = sorname
                    else:
                        validation = False
                if validation == False:
                    out_dict['form'] = ClientForm()
                    out_dict['ErrorMessage'] = error_message
                    return render(request, 'MedApp/registration-client.html', out_dict)
                client.user_id = auth.get_user(request).id
                client.token = token_str
                client.registration_date = datetime.today().strftime('%Y-%m-%d %H:%M')
                client.save()
                url = url + token_str + '&'
                return redirect(url)
            else:
                out_dict['ErrorMessage'] = error_message
                out_dict['form'] = ClientForm()
                return render(request, 'MedApp/registration-client.html', out_dict)
        else:
            out_dict['form'] = ClientForm()
        return render(request, 'MedApp/registration-client.html', out_dict)
    else:
        return redirect('/')
#(end)

def adding_client(request):
    out_dict = dict()
    session_key = request.session.session_key
    print(request.POST)
    return JsonResponse(out_dict)

#Services page(start)
def service(request, client_token):
    if auth.get_user(request).is_active:
        out_dict = {}
        user_id = auth.get_user(request).id
        out_dict['medapp_active'] = True
        out_dict['ServicesList'] = Usluga.objects.filter(user_id = user_id)
        out_dict['Client'] = Client.objects.get(token = client_token)
        url = '/medapp/clients/' + str(client_token) + '/'
        return render(request, 'MedApp/service.html', out_dict)
    else:
        return redirect('/')
#(end)

#Regstration service for client(start)
def registration_client_service(request, client_token, service_token):
    if auth.get_user(request).is_active:
        out_dict = {}
        # Token
        token = []
        token_join = ''
        for x in range(8):
            sym = random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
            token.append(sym)
        token_str = token_join.join(token)
        error_message = 'Введены не правильные данные'
        validation = True
        user_id = auth.get_user(request).id
        out_dict['medapp_active'] = True
        out_dict['Titles'] = Usluga.objects.filter(user_id = user_id)
        url = '/medapp/clients/' + str(client_token) + '&'
        if request.method == 'POST':
            form = ServiceForm(request.POST)
            medicine = request.POST.get('medicine', '')
            info = request.POST.get('info', '')
            client_id = Client.objects.get(token = client_token).id
            '''if medicine == '':
                medicine = 'Не указано'
                form.is_valid() == True
            if info == '':
                info = 'Не указано'
                form.is_valid() == True'''
            if form.is_valid():
                service = form.save(commit=False)
                service.foreign_key_id = client_id
                service.info = info
                service.medicine = medicine
                service.token = token_str
                service.title_id = Usluga.objects.get(token = service_token).id
                service.user_id = auth.get_user(request).id
                service.save()
                return redirect(url)
        else:
            out_dict['form'] = ServiceForm()
        return render(request, 'MedApp/create-service.html', out_dict)
    else:
        return redirect('/')
#(end)

#Create new service(start)
def create_new_service(request):
    if auth.get_user(request).is_active:
        out_dict = {}
        url = '/medapp/create-new-service/'
        # Token
        token_url = []
        url_join = ''
        for x in range(8):
            sym = random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
            token_url.append(sym)
        token = url_join.join(token_url)
        user_id = auth.get_user(request).id
        out_dict['medapp_active'] = True
        out_dict['ServicesList'] = Usluga.objects.filter(user_id = user_id)
        if request.method == 'POST':
            form = CreateNewServiceForm(request.POST)
            if form.is_valid():
                create_new_service = form.save(commit=False)
                create_new_service.user_id = user_id
                create_new_service.token = token
                create_new_service.save()
                return redirect(url)
        else:
            out_dict['form'] = CreateNewServiceForm()
        return render(request, 'MedApp/create-new-service.html', out_dict)
    else:
        return redirect('/')
#(end)

#DELETE
def delete_client(request, client_token):
    if auth.get_user(request).is_active:
        url = '/medapp/clients/'
        Client.objects.get(token = client_token).delete()
        return redirect(url)
    else:
        return redirect('/')

def delete_service(request, service_token):
    if auth.get_user(request).is_active:
        url = '/medapp/create-new-service/'
        Usluga.objects.get(token = service_token).delete()
        return redirect(url)
    else:
        return redirect('/')

def delete_client_service(request, client_token, service_client_token):
    if auth.get_user(request).is_active:
        out_dict = {}
        url = '/medapp/clients/' + client_token + '&'
        UslugaDlaClienta.objects.get(token = service_client_token).delete()
        return redirect(url)
    else:
        return redirect('/')

#EDIT

def edit_client(request, client_token):
    if auth.get_user(request).is_active:
        user_validation = False
        if auth.get_user(request).id == Client.objects.get(token=client_token).user_id:
            out_dict = {}
            error_message = 'Введены не правильные данные'
            validation = True
            url = '/medapp/clients/' + str(client_token) + '&'
            out_dict['medapp_active'] = True
            out_dict['User'] = auth.get_user(request)
            out_dict['Client'] = Client.objects.get(token=client_token)
            out_dict['BirthdayStr'] = Client.objects.get(token = client_token).birthday.strftime('%Y-%m-%d')
            if request.method == 'POST':
                new_name = request.POST.get('name', '')
                new_sorname = request.POST.get('sorname', '')
                new_number = request.POST.get('number', '')
                new_birthday = request.POST.get('birthday', '')
                new_info = request.POST.get('info', '')
                client = Client.objects.get(token = client_token)
                #if ValueError:
                 #   validation = False
                #Name validation TRUE
                if new_name.isalpha():
                    edit_new_name = new_name.lower()
                    new_name = edit_new_name[0].upper() + edit_new_name[1:]
                    client.name = new_name
                else:
                    validation = False
                #Sorname validation True
                if new_sorname.isalpha():
                    edit_new_sorname = new_sorname.lower()
                    new_sorname = edit_new_sorname[0].upper() + edit_new_sorname[1:]
                    client.sorname = new_sorname
                else:
                    validation = False
                #Number validation TRUE
                if new_number != '':
                    if len(new_number) == LENGTH_NUMBER:
                        client.number = new_number
                    else:
                        validation = False
                #Date validation True
                if datetime.strptime(new_birthday, TIME_FORMAT) < MAX_DATE:
                    if datetime.strptime(new_birthday, TIME_FORMAT) > MIN_DATE:
                        client.birthday = new_birthday
                    else:
                        validation = False
                else:
                    validation = False
                #Validation
                if validation == False:
                    out_dict['ErrorMessage'] = error_message
                    return render(request, 'MedApp/edit/edit-client-info.html', out_dict)
                client.info = new_info
                client.save(update_fields = ['name', 'sorname', 'number', 'birthday', 'info'])
                return redirect(url)
            else:
                return render(request, 'MedApp/edit/edit-client-info.html', out_dict)
        else:
            return redirect('/')
    else:
        return redirect('/')
    return render(request, 'MedApp/edit/edit-client-info.html', out_dict)

#USER PROFILE
def user_profile(request):
    if auth.get_user(request).is_active:
        out_dict = {}
        out_dict['User'] = auth.get_user(request)
        if request.method == 'POST':
            user = auth.get_user(request).check_password()
            old_password = request.POST.get('old_password', '')
            if user == old_password:
                pass
        return render(request, 'MedApp/edit/edit-profile.html', out_dict)
    else:
        return redirect('/')


def find(request):
    out_dict = {}
    return render(request, 'MedApp/find.html', out_dict)