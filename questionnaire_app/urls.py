from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^home/$', views.index, name='index'),
    url('^login/$', auth_views.login, {'template_name': 'registration/login.html'}),
    url('^logout/$', auth_views.logout, {'template_name': 'registration/logout.html'}),
    url('^change-password/$', auth_views.password_change, {'template_name': 'registration/password_change.html'}),
    url('^password-change-done/&', auth_views.password_change_done, {'template_name': 'registration/password_change_done.html'})
]
