from django.conf.urls import url
from . import views

#
urlpatterns = [
    url(r'^$', views.bike, name='index'),
    url(r'^(?P<v_id>[0-9]+)/$', views.details, name='details'),
]