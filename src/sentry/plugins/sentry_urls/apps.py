from __future__ import absolute_import

from django.apps import AppConfig


class PluginsSentryUrlsAppConfig(AppConfig):
    name = "sentry.plugins.sentry_urls"

    def ready(self):
        # XXX: this should semantically be .plugins
        from .models import UrlsPlugin
        from sentry.plugins import register

        register(UrlsPlugin)
