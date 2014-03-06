'''
Created on Feb 6, 2014

@author: agoncalves
@email: viner_lipe@hotmail.com
'''

from django.conf.urls import patterns, url

urlpatterns = patterns('configuration.views',
     url(r'^/enterprise/list[/]?$', 'enterprise_list', name='enterprise_list'),
     url(r'^/enterprise/edit[/]?$', 'enterprise_edit', name='enterprise_edit'),
     url(r'^/enterprise/add[/]?$', 'enterprise_add', name='enterprise_add'),
     url(r'^/enterprise/ajax/list[/]?$', 'enterprise_ajax_list', name='enterprise_ajax_list'),
     url(r'^/enterprise/ajax/save[/]?$', 'enterprise_ajax_save', name='enterprise_ajax_save'),
     url(r'^/enterprise/ajax/toogle_status[/]?$', 'enterprise_ajax_toogle_status', name='enterprise_ajax_toogle_status'),

     url(r'^/user/list[/]?$', 'user_list', name='user_list'),
     #url(r'^/user/edit[/]?$', 'user_edit', name='user_edit'),
     url(r'^/user/add[/]?$', 'user_add', name='user_add'),
     url(r'^/user/ajax/list[/]?$', 'user_ajax_list', name='user_ajax_list'),
     url(r'^/user/ajax/save[/]?$', 'user_ajax_save', name='user_ajax_save'),
)
