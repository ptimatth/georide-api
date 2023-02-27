"""
Georide objects implementation
@author Matthieu DUVAL <matthieu@duval-dev.fr>
"""
import time
import logging

_LOGGER = logging.getLogger(__name__)

class GeoRideAccount:
    """ Account object representation """ 
    def __init__(self, account_id, email, is_admin, auth_token):
        self._account_id = account_id
        self._email = email
        self._is_admin = is_admin
        self._auth_token = auth_token

    @property
    def account_id(self):
        """ account_id """
        return self._account_id

    @property
    def email(self):
        """ email """
        return self._email

    @property
    def is_admin(self):
        """ is_admin """
        return self._is_admin

    @property
    def auth_token(self):
        """ auth_token """
        return self._auth_token

    @auth_token.setter
    def auth_token(self, new_token):
        """ change auth_token """
        self._auth_token = new_token

    @staticmethod
    def from_json(json):
        """return new object from_json"""
        return GeoRideAccount(
            json['id'],
            json['email'],
            json['isAdmin'],
            json['authToken']
        )