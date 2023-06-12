import os
import pkgutil

from .. import constants


def initialize_environment():
    """Initialize environment for vila."""
    if not os.path.exists(constants.CONFIG_PATH):
        with open(constants.CONFIG_PATH, 'wb') as f:
            default_config_data = pkgutil.get_data('vila', 'resources/default_config.yml')
            f.write(default_config_data)