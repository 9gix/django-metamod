from django.contrib.admin import ModelAdmin
from django.conf.urls import patterns, url
from functools import update_wrapper
from django.shortcuts import render

class ModelModeration(ModelAdmin):
    moderation_template = None

    def get_urls(self):
        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)
            return update_wrapper(wrapper, view)

        model_meta = self.model._meta
        info = model_meta.app_label, model_meta.module_name

        urlpatterns = patterns('',
            url(r'^$',
                wrap(self.moderation_view),
                name='%s_%s_changelist' %info),
        )
        return urlpatterns

    def moderation_view(self, request):
        data = {}
        template = self.moderation_template or [
            'metamod/%s/%s/moderation_panel.html',
            'metamod/%s/moderation_panel.html',
            'metamod/moderation_panel.html']
        return render(request, template, data)
