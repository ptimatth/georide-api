"""
Georide objects implementation
@author Matthieu DUVAL <matthieu@duval-dev.fr>
"""
import time
import logging

_LOGGER = logging.getLogger(__name__)

class GeoRideTrackerTrip:  # pylint: disable=too-many-instance-attributes
    """ Trip object representation """
    def __init__(self, trip_id, tracker_id, average_speed, max_speed, distance, duration, # pylint: disable=R0914, R0913
                 start_address, nice_start_address, start_lat, start_lon, end_address,
                 nice_end_address, end_lat, end_lon, start_time, end_time): 
        self._trip_id = trip_id
        self._tracker_id = tracker_id
        self._average_speed = average_speed
        self._max_speed = max_speed
        self._distance = distance
        self._duration = duration
        self._start_address = start_address
        self._nice_start_address = nice_start_address
        self._start_lat = start_lat
        self._start_lon = start_lon
        self._end_address = end_address
        self._nice_end_address = nice_end_address
        self._end_lat = end_lat
        self._end_lon = end_lon
        self._start_time = start_time
        self._end_time = end_time
    
    
    @property
    def trip_id(self):
        """trip_id  """
        return self._trip_id
    
    @property
    def tracker_id(self):
        """ tracker_id """
        return self._tracker_id
    
    @property
    def average_speed(self):
        """ average_speed """
        return self._average_speed
    
    @property
    def max_speed(self):
        """ max_speed """
        return self._max_speed
    
    @property
    def distance(self):
        """ distance """
        return self._distance
    
    @property
    def duration(self):
        """ duration """
        return self._duration
    
    @property
    def start_address(self):
        """ start_address """
        return self._start_address
    
    @property
    def nice_start_address(self):
        """ nice_start_address """
        return self._nice_start_address
    
    @property
    def start_lat(self):
        """ start_lat """
        return self._start_lat
    
    @property
    def start_lon(self):
        """ start_lon """
        return self._start_lon
    
    @property
    def end_address(self):
        """ end_address """
        return self._end_address
    
    @property
    def nice_end_address(self):
        """ nice_end_address """
        return self._nice_end_address
    
    @property
    def end_lat(self):
        """end_lat  """
        return self._end_lat
    
    @property
    def end_lon(self):
        """end_lon  """
        return self._end_lon
    
    @property
    def start_time(self):
        """ start_time """
        return self._start_time
    
    @property
    def end_time(self):
        """ end_time """
        return self._end_time

    
    @staticmethod
    def from_json(json):
        """return new object from json"""
        return GeoRideTrackerTrip(
            json['id'],
            json['trackerId'],
            json['averageSpeed'],
            json['maxSpeed'],
            json['distance'],
            json['duration'],
            json['startAddress'],
            json['niceStartAddress'],
            json['startLat'],
            json['startLon'],
            json['endAddress'],
            json['niceEndAddress'],
            json['endLat'],
            json['endLon'],
            json['startTime'],
            json['endTime']
        )