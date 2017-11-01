from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^interval/', views.interval),
    url(r'^last-month/$', views.calculate_month),
    url(r'^last-week/$', views.calculate_week),
    url(r'^last-day/$', views.calculate_yesterday),
    url(r'^today/$', views.calculate_today),
    url(r'^$', views.calculate_menu),
]