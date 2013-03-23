from django.conf.urls import patterns, include, url
from django.contrib import admin
import metamod

admin.autodiscover()
metamod.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
