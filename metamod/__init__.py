import copy
from django.conf import settings
from metamod.panels import panel
from metamod.options import ModelModeration


def autodiscover():
    import imp
    from django.utils.importlib import import_module
    for app in settings.INSTALLED_APPS:
        try:
            import_module('%s.moderation' % app)
        except:
            pass
