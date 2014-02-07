from django.conf.urls import patterns, url

urlpatterns = patterns('configuration.views',
     url(r'^/enterprise/list[/]?$', 'enterprise_list', name='enterprise_list'),
     url(r'^/enterprise/edit[/]?$', 'enterprise_edit', name='enterprise_edit'),
     url(r'^/enterprise/add[/]?$', 'enterprise_add', name='enterprise_add'),
     url(r'^/enterprise/ajax/list[/]?$', 'enterprise_ajax_list', name='enterprise_ajax_list'),
     url(r'^/enterprise/ajax/save[/]?$', 'enterprise_ajax_save', name='enterprise_ajax_save'),
)
