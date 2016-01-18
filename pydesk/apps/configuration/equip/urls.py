# coding: utf-8

from django.conf.urls import patterns, url

urlpatterns = patterns('pydesk.apps.configuration.equip.views',
     url(r'^/list[/]?$', 'equip_list', name='equip_list'),
     url(r'^/edit[/]?$', 'equip_edit', name='equip_edit'),
     url(r'^/add[/]?$', 'equip_add', name='equip_add'),
     url(r'^/ajax/list[/]?$', 'equip_ajax_list', name='equip_ajax_list'),
     url(r'^/ajax/save[/]?$', 'equip_ajax_save', name='equip_ajax_save'),
     url(r'^/ajax/toogle_status[/]?$', 'equip_ajax_toogle_status', name='equip_ajax_toogle_status'),
)
