from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView

from .forms import RegisterForm
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('^register/$',
        CreateView.as_view(template_name='registration/register.html',
                           form_class=RegisterForm,
                           success_url='/login')),
    url('^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    url('^logout/$', auth_views.logout, {'template_name': 'registration/logged_out.html'}),
    url('^change-password/$', auth_views.password_change, {'template_name': 'registration/password_change.html',
                                                           'post_change_redirect': '/password-change-done'}),
    url('^password-change-done/$', auth_views.password_change_done,
        {'template_name': 'registration/password_change_done.html'}),
]
