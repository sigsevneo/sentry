from __future__ import absolute_import

from .bindings import BindingManager
from .manager import PluginManager
from .notifier import *  # NOQA
from .response import *  # NOQA
from .structs import *  # NOQA
from .v1 import *  # NOQA
from .v2 import *  # NOQA

# TODO: hoist these up to sentry.plugins.
# I know this won't work, but can't test this until I block pytest rev-up.
bindings = BindingManager()

plugins = PluginManager()
register = plugins.register
unregister = plugins.unregister
