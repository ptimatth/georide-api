"""
Georide objects implementation
@author Matthieu DUVAL <matthieu@duval-dev.fr>
"""
import time
import logging
from . import JsonMgtMetaClass

_LOGGER = logging.getLogger(__name__)

class GeoRideSubscription_CardInfo(metaclass=JsonMgtMetaClass):
    """ Account object representation """ 
    def __init__(self, last_digits, expiry, brand):
        self._last_digits = last_digits
        self._expiry = expiry
        self._brand = brand
   
    @property
    def last_digits(self):
        """last_digits property"""
        return self._last_digits

    @property
    def expiry(self):
        """expiry property"""
        return self._expiry

    @property
    def brand(self):
        """brand property"""
        return self._brand


    @classmethod
    def from_json(cls, json):
        """return new object from_json"""
        return GeoRideSubscription_CardInfo(
            cls.json_field_protect(json, 'lastDigits'),
            cls.json_field_protect(json, 'expiry'),
            cls.json_field_protect(json, 'brand')
        )