from django.contrib import admin
from metamod.options import ModelModeration
from metamod.models import Moderation


class ModerationPanel(object):
    def __init__(self):
        pass

    def register(self, model, moderation_class=None):
        if not moderation_class:
            moderation_class = ModelModeration

        Meta = type('Meta', (), {'proxy': True, 'app_label': 'Moderation', 'verbose_name_plural': model._meta.verbose_name_plural})

        options = {'__module__': 'metamod.models', 'Meta': Meta}
        proxy_model = type(model.__name__, (model,), options)
        admin.site.register(proxy_model, moderation_class)

panel = ModerationPanel()
