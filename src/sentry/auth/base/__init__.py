from __future__ import absolute_import

import sentry.options as options
from sentry.auth.providers.google.provider import GoogleOAuth2Provider
from sentry.auth.manager import ProviderManager
from sentry.auth.view import *  # NOQA

# TODO: hoist these up to sentry.auth.
# I know this won't work, but can't test this until I block pytest rev-up.

manager = ProviderManager()
register = manager.register
unregister = manager.unregister

register("google", GoogleOAuth2Provider)

options.register(
    "auth-google.client-id", flags=options.FLAG_ALLOW_EMPTY | options.FLAG_PRIORITIZE_DISK
)
options.register(
    "auth-google.client-secret", flags=options.FLAG_ALLOW_EMPTY | options.FLAG_PRIORITIZE_DISK
)
