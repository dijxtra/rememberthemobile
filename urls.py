from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'views.index', name='home'),

    url(r'^(?P<id>\d+)/edit/$', 'views.edit', name='edit'),
    url(r'^(?P<id>\d+)/postpone/$', 'views.postpone', name='postpone'),
    url(r'^(?P<id>\d+)/complete/$', 'views.complete', name='complete'),

    url(r'^prev_day/$', 'views.prev_day', name='prev_day'),
    url(r'^next_day/$', 'views.next_day', name='next_day'),
    # Example:
    # (r'^rtm/', include('rtm.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
