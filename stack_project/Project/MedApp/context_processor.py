from django.template import loader, RequestContext
from MedApp.models import Client
from django.contrib import auth

def application_info_processor(request):
    base_info = {}
    user = auth.get_user(request)
    base_info['medapp_active'] = True
    base_info['User'] = user
    base_info['Clients'] = Client.objects.filter(user_id = user.id)
    return (base_info)