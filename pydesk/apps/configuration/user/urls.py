# coding: utf-8

from django.conf.urls import patterns, url

urlpatterns = patterns('pydesk.apps.configuration.user.views',
     url(r'^/list[/]?$', 'user_list', name='user_list'),
     #url(r'^/user/edit[/]?$', 'user_edit', name='user_edit'),
     url(r'^/add[/]?$', 'user_add', name='user_add'),
     url(r'^/ajax/list[/]?$', 'user_ajax_list', name='user_ajax_list'),
     url(r'^/ajax/save[/]?$', 'user_ajax_save', name='user_ajax_save'),
)