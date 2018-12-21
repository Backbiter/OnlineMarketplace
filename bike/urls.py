from django.conf.urls import url
from . import views

app_name = 'bike'

#
urlpatterns = [
    url(r'^$', views.bike, name='index'),

    #/bike/2/
    url(r'^(?P<pk>[0-9]+)/$', views.details, name='details'),

    #/bike/add/
    url(r'^add/$', views.BikeInsert.as_view(), name='bike-add'),
]
