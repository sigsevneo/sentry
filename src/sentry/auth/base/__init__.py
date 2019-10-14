from __future__ import absolute_import

from sentry.auth.provider import *  # NOQA
from sentry.auth.manager import ProviderManager
from sentry.auth.view import *  # NOQA

# TODO: hoist these up to sentry.auth.
# I know this won't work, but can't test this until I block pytest rev-up.

manager = ProviderManager()
register = manager.register
unregister = manager.unregister
