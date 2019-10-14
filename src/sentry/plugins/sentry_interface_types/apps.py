from __future__ import absolute_import

from django.apps import AppConfig


class PluginsSentryInterfaceTypesAppConfig(AppConfig):
    name = "sentry.plugins.sentry_interface_types"

    def ready(self):
        # XXX: this should semantically be .plugins
        from .models import InterfaceTypePlugin
        from sentry.plugins.base import register

        register(InterfaceTypePlugin)
