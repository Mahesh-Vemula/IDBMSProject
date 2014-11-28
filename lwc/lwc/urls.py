from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'movietickets.views.index', name='home'),
    url(r'^testpage', 'lwc.views.testpage', name='testpage'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^movietickets/', include('movietickets.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
