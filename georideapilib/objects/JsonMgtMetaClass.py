"""
Georide objects implementation
@author Matthieu DUVAL <matthieu@duval-dev.fr>
"""
import time
import logging

_LOGGER = logging.getLogger(__name__)

class JsonMgtMetaClass(type):
    @staticmethod
    def json_field_protect(json, field_name, default_value = None):
        return json[field_name] if field_name in json.keys() else default_value