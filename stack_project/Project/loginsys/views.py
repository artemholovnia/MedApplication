from django.shortcuts import render, redirect
from django.contrib import auth
from django.views.decorators import csrf

# Create your views here.

def login(request):
    out_dict = {}
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            out_dict['User'] = auth.get_user(request).username
            return redirect('/')
        else:
            out_dict['login_error'] = 'Пользователь не найден'
            return render(request, 'loginsys/login.html', out_dict)
    else:
        return render(request, 'loginsys/login.html', out_dict)

def logout(request):
    auth.logout(request)
    return redirect('/')

def queslogout(request):
    out_dict = {}
    out_dict['User'] = auth.get_user(request).username
    return render(request, 'loginsys/login.html', out_dict)
