from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hsh_demo.views.home', name='home'),
    # url(r'^hsh_demo/', include('hsh_demo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'core.views.home'),
    url(r'^add_user/$', 'core.views.add_user'),
    url(r'^del_user/(\d+)/$', 'core.views.del_user'),
)
