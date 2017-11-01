from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^create-new-service/(?P<service_token>\w+)!-delete-service/', views.delete_service),
    url(r'^clients/(?P<client_token>\w+)/edit-client/', views.edit_client),

    ####with &
    url(r'^clients/(?P<client_token>\w+)/delete-client/$', views.delete_client),
    url(r'^clients/(?P<client_token>\w+)&service&(?P<service_token>\w+)&registration-client-service/', views.registration_client_service),
    url(r'^clients/(?P<client_token>\w+)&service&', views.service),
    url(r'^clients/(?P<client_token>\w+)&(?P<service_client_token>\w+)&delete-client-service/', views.delete_client_service),
    url(r'^clients/(?P<client_token>\w+)&$', views.client_info),
    ####

    url(r'^clients/', views.clients),
    url(r'^registration-client/', views.registration_client, name='registration-client'),
    url(r'^adding_client/', views.adding_client, name='adding_client'),
    url(r'^create-new-service/', views.create_new_service),
    url(r'^edit-profile/', views.user_profile),

    #url(r'^search-client/$', views.search_client)
]



