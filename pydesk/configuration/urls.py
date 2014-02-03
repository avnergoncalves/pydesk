from django.conf.urls import patterns, url

urlpatterns = patterns('configuration.views',
     url(r'^/enterprise/list[/]?$', 'enterprise_list', name='enterprise_list'),
     url(r'^/enterprise/add[/]?$', 'enterprise_add', name='enterprise_add'),
     url(r'^/ajax_enterprise_list[/]?$', 'ajax_enterprise_list', name='ajax_enterprise_list'),
     url(r'^/ajax_enterprise_save[/]?$', 'ajax_enterprise_save', name='ajax_enterprise_save'),
)
