# -*- coding: utf-8 -*-
import os

from lektor.pluginsystem import Plugin

from everett.manager import (
    ConfigManager,
    ConfigOSEnv,
    ConfigIniEnv
)


class ExtraConfigPlugin(Plugin):
    name = u'extra-config'
    description = u'Adds config template function for accessing env variables.'

    def on_setup_env(self, **extra):
        config = ConfigManager([
            ConfigOSEnv(),
            ConfigIniEnv([
                os.environ.get('LEKTOR_EXTRA_CONFIG_INI'),
            ])
        ])
        self.env.jinja_env.globals['config'] = config
