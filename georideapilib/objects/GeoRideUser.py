"""
Georide objects implementation
@author Matthieu DUVAL <matthieu@duval-dev.fr>
"""
import time
import logging

_LOGGER = logging.getLogger(__name__)

class GeoRideUser: # pylint: disable= R0902
    """ User object representation """ 
    def __init__(self, user_id, email, first_name, created_at, phone_number, # pylint: disable= R0913
                 push_user_token, legal, date_of_birth): 
        self._user_id = user_id
        self._email = email
        self._first_name = first_name
        self._created_at = created_at
        self._phone_number = phone_number
        self._push_user_token = push_user_token
        self._legal = legal
        self._date_of_birth = date_of_birth

    @property
    def user_id(self):
        """ user_id """
        return self._user_id

    @property
    def email(self):
        """ email """
        return self._email

    @property
    def first_name(self):
        """ first_name """
        return self._first_name

    @property
    def created_at(self):
        """ created_at """
        return self._created_at
    
    @property
    def phone_number(self):
        """ phone_number """
        return self._phone_number
    
    @property
    def push_user_token(self):
        """ push_user_token """
        return self._push_user_token
    
    @property
    def legal(self):
        """ legal """
        return self._legal

    @property
    def date_of_birth(self):
        """ date_ofo_birth """
        return self._date_of_birth

    @staticmethod
    def from_json(json):
        """return new object fromjson"""
        return GeoRideUser(
            json['id'],
            json['email'],
            json['firstName'],
            json['createdAt'],
            json['phoneNumber'],
            json['pushUserToken'],
            json['legal'],
            json['dateOfBirth']
        )