'''
Created on Feb 6, 2014

@author: agoncalves
@email: viner_lipe@hotmail.com
'''

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     url(r'^$', 'accounts.views.login', name='login'),

     url(r'^accounts', include('accounts.urls')),
     url(r'^dashboard', include('dashboard.urls')),
     url(r'^configuration', include('configuration.urls')),
)
