from __future__ import absolute_import

from django.apps import AppConfig


class AuthAppConfig(AppConfig):
    name = "sentry.auth"

    def ready(self):
        from sentry.auth.base import *  # NOQA
