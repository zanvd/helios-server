"""
taken from

http://www.djangosnippets.org/snippets/377/

and adapted to LDObject
"""

import datetime
import json
from django.db import models
from django.db.models import signals
from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder

from numbers import Number
from django.contrib.postgres.fields import JSONField
from django.contrib.postgres.fields.jsonb import JsonAdapter

from . import LDObject

class LDObjectField(JSONField):
    """
    LDObject is a generic textfield that neatly serializes/unserializes
    JSON objects seamlessly.
    """

    description = "A LDObject"

    def __init__(self, type_hint=None, **kwargs):
        self.type_hint = type_hint
        super(LDObjectField, self).__init__(**kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(LDObjectField, self).deconstruct()
        if self.type_hint is not None:
            kwargs['type_hint'] = self.type_hint
        return name, path, args, kwargs

    def from_db_value(self, value, expression, connection, context):
        """Convert our value to LDObject after we load it from the DB"""
        #value = super(LDObjectField, self).from_db_value(value, expression, connection, context)
        if value is None:
            return None

        "we give the wrapped object back because we're not dealing with serialization types"
        return LDObject.fromDict(value, type_hint = self.type_hint).wrapped_obj

    def to_python(self, value):
        """Convert value to LDObject"""

        # did we already convert this?
        if not isinstance(value, (str, Number, dict, list, bool)):
            return value

        value = super(LDObjectField, self).to_python(value)

        "we give the wrapped object back because we're not dealing with serialization types"
        return LDObject.fromDict(value, type_hint = self.type_hint).wrapped_obj

    def get_prep_value(self, value):
        """Convert our JSON object to a string before we save"""
        if isinstance(value, JsonAdapter):
            return value

        if value is None:
            return None

        # instantiate the proper LDObject to dump it appropriately
        ld_object = LDObject.instantiate(value, datatype=self.type_hint)
        return super(LDObjectField, self).get_prep_value(ld_object.toDict(complete = True))
