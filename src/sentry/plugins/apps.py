from __future__ import absolute_import

from django.apps import AppConfig


class PluginsAppConfig(AppConfig):
    name = "sentry.plugins"

    def ready(self):
        pass
#        from sentry.plugins.base import *  # NOQA
#        from sentry.plugins.bases import *  # NOQA
#        from sentry.plugins.interfaces import *  # NOQA
