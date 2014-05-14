# coding: utf-8

from django.conf.urls import patterns, url

urlpatterns = patterns('pydesk.apps.dashboard.views',
     url(r'^/home[/]?$', 'home', name='home'),
)
