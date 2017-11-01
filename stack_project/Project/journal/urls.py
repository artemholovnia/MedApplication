from django.conf.urls import url
from . import views
from calculate.views import calculate_date

urlpatterns = [
    url(r'^calculate&(?P<date>\w+\W+)$', calculate_date),
    url(r'^all-clients&', views.journal),

    #url(r'^search-client/$', views.search_client)
]



