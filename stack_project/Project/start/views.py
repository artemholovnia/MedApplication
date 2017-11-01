from django.shortcuts import render, redirect
from django.contrib import auth

# Create your views here.

def start(request):
    out_dict = {}
    if auth.get_user(request).is_active == True:
        out_dict['User'] = auth.get_user(request)
        out_dict['startapp_active'] = True
        return render(request, 'start/start.html', out_dict)
    else:
        return redirect('/auth/login/')

