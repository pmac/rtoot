# -*- coding: utf-8 -*-
import csv
from io import StringIO

from lektor.pluginsystem import Plugin
from lektor.types import Type


def csv_to_dicts(text):
    text = text.strip()
    if text:
        return csv.DictReader(StringIO(text), skipinitialspace=True)


class CsvType(Type):
    widget = 'multiline-text'

    def value_from_raw(self, raw):
        return csv_to_dicts(raw.value or u'')


class CsvFieldPlugin(Plugin):
    name = u'csv-field'
    description = u'Add a CSV field type for models.'

    def on_setup_env(self):
        self.env.add_type(CsvType)
