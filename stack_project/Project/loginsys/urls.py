from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/', views.login),
    url(r'^logout/', views.logout),

]
#url(r'^plans/plan/', views.plan)
'''url(r'^lessons/(?P<lesson_id>[0-9]+)/$', views.lessons)'''