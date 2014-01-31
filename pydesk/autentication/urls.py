from django.conf.urls import patterns, include, url

urlpatterns = patterns('autentication.views',
    # Examples:
     url(r'^/login[/]?$', 'login', name='login'),
     url(r'^/logout[/]?$', 'logout', name='logout'),
    # url(r'^blog/', include('blog.urls')),
)
