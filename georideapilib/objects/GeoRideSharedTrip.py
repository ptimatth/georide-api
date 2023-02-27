"""
Georide objects implementation
@author Matthieu DUVAL <matthieu@duval-dev.fr>
"""
import time
import logging


_LOGGER = logging.getLogger(__name__)

class GeoRideSharedTrip:
    """ Shared trip object representation """
    def __init__(self, url, shareId):
        self._url = url
        self._share_id = shareId

    @property
    def url(self):
        """ shared trip url """
        return self._url
    
    @property
    def share_id(self):
        """ shared trip id """
        return self._share_id

    @staticmethod
    def from_json(json):
        """return new object fromjson"""
        return GeoRideSharedTrip(
            json['url'],
            json['shareId']
        )