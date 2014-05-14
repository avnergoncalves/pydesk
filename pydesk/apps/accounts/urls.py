# coding: utf-8

from django.conf.urls import patterns, url

urlpatterns = patterns('pydesk.apps.accounts.views',
     url(r'^/login[/]?$', 'login', name='login'),
     url(r'^/logout[/]?$', 'logout', name='logout'),
    # url(r'^blog/', include('blog.urls')),
)
