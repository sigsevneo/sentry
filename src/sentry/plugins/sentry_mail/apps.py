from __future__ import absolute_import

from django.apps import AppConfig


class PluginsSentryMailAppConfig(AppConfig):
    name = "sentry.plugins.sentry_mail"

    def ready(self):
        # XXX: this should semantically be .plugins
        from .models import MailPlugin
        from sentry.plugins import register

        register(MailPlugin)
