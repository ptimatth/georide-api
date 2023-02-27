"""
Georide objects implementation
@author Matthieu DUVAL <matthieu@duval-dev.fr>
"""
import time
import logging
from . import JsonMgtMetaClass, GeoRideSubscription_CardInfo

_LOGGER = logging.getLogger(__name__)

class GeoRideSubscription(metaclass=JsonMgtMetaClass):
    """ Account object representation """ 
    def __init__(self, subscription_id, subscription_type, initial_date, next_payment_date,
                status, paused_since, cancel_requested, price, first_name, last_name, card_information):
        self._subscription_id = subscription_id
        self._subscription_type = subscription_type
        self._initial_date = initial_date
        self._next_payment_date = next_payment_date
        self._status = status
        self._paused_since = paused_since
        self._cancel_requested = cancel_requested
        self._price = price
        self._first_name = first_name
        self._last_name = last_name
        self._card_information = card_information

    @property
    def subscription_id(self):
        """subscription_id property"""
        return self._subscription_id

    @property
    def subscription_type(self):
        """subscription_type property"""
        return self._subscription_type

    @property
    def initial_date(self):
        """initial_date property"""
        return self._initial_date

    @property
    def next_payment_date(self):
        """next_payment_date property"""
        return self._next_payment_date

    @property
    def status(self):
        """status property"""
        return self._status

    @property
    def paused_since(self):
        """paused_since property"""
        return self._paused_since

    @property
    def cancel_requested(self):
        """cancel_requested property"""
        return self._cancel_requested

    @property
    def price(self):
        """price property"""
        return self._price

    @property
    def first_name(self):
        """first_name property"""
        return self._first_name

    @property
    def last_name(self):
        """last_name property"""
        return self._last_name

    @property
    def card_information(self):
        """card_information property"""
        return self._card_information

    @classmethod
    def from_json(cls, json):
        """return new object from_json"""
        card_info = GeoRideSubscription_CardInfo.from_json(json['cardInformation']) if cls.json_field_protect(json, 'cardInformation', None) is not None else {}
        return GeoRideSubscription(
            cls.json_field_protect(json, 'id', -1),
            json['type'],
            cls.json_field_protect(json, 'initialDate'),
            cls.json_field_protect(json, 'nextPaymentDate'),
            cls.json_field_protect(json, 'status'),
            cls.json_field_protect(json, 'pausedSince'),
            cls.json_field_protect(json, 'cancelRequested'),
            cls.json_field_protect(json, 'price'),
            cls.json_field_protect(json, 'firstName'),
            cls.json_field_protect(json, 'lastName'),
            card_info
        )