'''
Created on Feb 6, 2014

@author: agoncalves
@email: viner_lipe@hotmail.com
'''

from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
     url(r'^$', 'pydesk.apps.accounts.views.login', name='login'),

     url(r'^accounts', include('pydesk.apps.accounts.urls')),
     url(r'^dashboard', include('pydesk.apps.dashboard.urls')),
     url(r'^configuration/enterprise', include('pydesk.apps.configuration.enterprise.urls')),
     url(r'^configuration/user', include('pydesk.apps.configuration.user.urls')),
     
     url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()