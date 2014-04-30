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
     url(r'^$', 'pydesk.accounts.views.login', name='login'),

     url(r'^accounts', include('pydesk.accounts.urls')),
     url(r'^dashboard', include('pydesk.dashboard.urls')),
     url(r'^enterprise', include('pydesk.enterprise.urls')),
     url(r'^user', include('pydesk.user.urls')),
     
     url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()