from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    url(r'^login/$', views.UserLogin.as_view(), name='login'),

    url(r'^logout/$', views.logout_user, name='user-logout'),

    url(r'^userinfo/$', views.UserInfoView.as_view(), name='user-info'),

    url(r'^trial/$', views.register, name='trial'),
]
