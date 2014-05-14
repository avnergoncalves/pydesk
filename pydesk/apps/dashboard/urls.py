'''
Created on Feb 6, 2014

@author: agoncalves
@email: viner_lipe@hotmail.com
'''

from django.conf.urls import patterns, url

urlpatterns = patterns('pydesk.apps.dashboard.views',
     url(r'^/home[/]?$', 'home', name='home'),
)
