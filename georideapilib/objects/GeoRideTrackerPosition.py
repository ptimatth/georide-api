"""
Georide objects implementation
@author Matthieu DUVAL <matthieu@duval-dev.fr>
"""
import time
import logging

_LOGGER = logging.getLogger(__name__)

class GeoRideTrackerPosition:
    """ Tracker position object representation """
    def __init__(self, fixtime, latitude, longitude, altitude, speed, address): # pylint: disable= R0913
        self._fixtime = fixtime
        self._latitude = latitude
        self._longitude = longitude
        self._altitude = altitude
        self._speed = speed
        self._address = address

    @property
    def fixtime(self):
        """ fixtime """
        return self._fixtime

    @property
    def latitude(self):
        """ latitude """
        return self._latitude

    @property
    def longitude(self):
        """ longitude """
        return self._longitude

    @property
    def altitude(self):
        """ altitude """
        return self._altitude

    @property
    def speed(self):
        """ speed (m/s) """
        return self._speed

    @property
    def address(self):
        """ address """
        return self._address

    @staticmethod
    def from_json(json):
        """return new object fromjson"""
        return GeoRideTrackerPosition(
            json['fixtime'],
            json['latitude'],
            json['longitude'],
            json['altitude'],
            json['speed'],
            json['address']
        )