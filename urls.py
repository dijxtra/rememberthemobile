from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'views.index', name='home'),

    url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$', 'views.day', name='day'),

    url(r'^action/$', 'views.action', name='action'),
    url(r'^(?P<list_id>\d+)/(?P<series_id>\d+)/(?P<task_id>\d+)/edit/$', 'views.edit', name='edit'),
    url(r'^(?P<list_id>\d+)/(?P<series_id>\d+)/(?P<task_id>\d+)/delete/$', 'views.delete', name='delete'),
    url(r'^(?P<list_id>\d+)/(?P<series_id>\d+)/(?P<task_id>\d+)/postpone/$', 'views.postpone', name='postpone'),
    url(r'^(?P<list_id>\d+)/(?P<series_id>\d+)/(?P<task_id>\d+)/complete/$', 'views.complete', name='complete'),

    url(r'^today$', 'views.today', name='today'),
    url(r'^prev_day$', 'views.prev_day', name='prev_day'),
    url(r'^next_day$', 'views.next_day', name='next_day'),

    # Example:
    # (r'^rtmob/', include('rtmob.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
