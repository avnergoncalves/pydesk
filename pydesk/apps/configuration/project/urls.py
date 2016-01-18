# coding: utf-8

from django.conf.urls import patterns, url

urlpatterns = patterns('pydesk.apps.configuration.project.views',
     url(r'^/list[/]?$', 'project_list', name='project_list'),
     url(r'^/edit[/]?$', 'project_edit', name='project_edit'),
     url(r'^/add[/]?$', 'project_add', name='project_add'),
     url(r'^/ajax/list[/]?$', 'project_ajax_list', name='project_ajax_list'),
     url(r'^/ajax/save[/]?$', 'project_ajax_save', name='project_ajax_save'),
     url(r'^/ajax/toogle_status[/]?$', 'project_ajax_toogle_status', name='project_ajax_toogle_status'),
)
