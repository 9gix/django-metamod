from django.contrib.admin import ModelAdmin
from django.conf.urls import patterns, url
from functools import update_wrapper
from django.shortcuts import render
from metamod.models import Action

class ModelModeration(ModelAdmin):
    moderation_template = None
    moderation_view = None

    def __init__(self, *args, **kwargs):
        super(ModelModeration, self).__init__(*args, **kwargs)
        self.moderation_actions = Action.objects.all()

    def get_urls(self):
        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)
            return update_wrapper(wrapper, view)

        model_meta = self.model._meta
        info = model_meta.app_label, model_meta.module_name

        urlpatterns = patterns('',
            url(r'^$',
                wrap(self.changelist_view),
                name='%s_%s_changelist' %info),
            url(r'^all/$',
                wrap(self.moderation_view),
                name='%s_%s_all' %info),
        )
        for action in self.moderation_actions:
            ul = url(r'^%s/$' % action.slug,
                wrap(self.moderation_view),
                name='%s_%s_%s' % (info[0], info[1], action.name.lower()))
            urlpatterns += patterns('', ul)
        return urlpatterns

    def changelist_view(self, request):
        data = {}
        moderation_actions = self.moderation_actions
        data['moderation_actions'] = moderation_actions
        template = self.change_list_template or [
            'metamod/%s/%s/moderation_board.html',
            'metamod/%s/moderation_board.html',
            'metamod/moderation_board.html']
        return render(request, template, data)

    def moderation_view(self, request):
        data = {}

        data['object_list'] = self.model._default_manager.all()

        template = self.moderation_template or [
            'metamod/%s/%s/moderation_panel.html',
            'metamod/%s/moderation_panel.html',
            'metamod/moderation_panel.html']
        return render(request, template, data)
