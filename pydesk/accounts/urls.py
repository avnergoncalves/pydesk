'''
Created on Feb 6, 2014

@author: agoncalves
@email: viner_lipe@hotmail.com
'''

from django.conf.urls import patterns, url

urlpatterns = patterns('pydesk.accounts.views',
     url(r'^/login[/]?$', 'login', name='login'),
     url(r'^/logout[/]?$', 'logout', name='logout'),
    # url(r'^blog/', include('blog.urls')),
)