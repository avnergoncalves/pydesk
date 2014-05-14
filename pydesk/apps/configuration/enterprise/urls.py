# coding: utf-8

from django.conf.urls import patterns, url

urlpatterns = patterns('pydesk.apps.configuration.enterprise.views',
     url(r'^/list[/]?$', 'enterprise_list', name='enterprise_list'),
     url(r'^/edit[/]?$', 'enterprise_edit', name='enterprise_edit'),
     url(r'^/add[/]?$', 'enterprise_add', name='enterprise_add'),
     url(r'^/ajax/list[/]?$', 'enterprise_ajax_list', name='enterprise_ajax_list'),
     url(r'^/ajax/save[/]?$', 'enterprise_ajax_save', name='enterprise_ajax_save'),
     url(r'^/ajax/toogle_status[/]?$', 'enterprise_ajax_toogle_status', name='enterprise_ajax_toogle_status'),
)
