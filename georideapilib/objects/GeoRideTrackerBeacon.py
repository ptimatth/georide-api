"""
Georide objects implementation
@author Matthieu DUVAL <matthieu@duval-dev.fr>
"""
import time
import logging
from . import JsonMgtMetaClass

_LOGGER = logging.getLogger(__name__)

class GeoRideTrackerBeacon:
    """ GeoRideTrackerBeacon representation """ 
    def __init__(self, beacon_id, linked_tracker_id, name, created_at, updated_at,
                 mac_address, battery_level, last_battery_level_update, sleep_delay,
                 is_updated, power):
        self._beacon_id = beacon_id
        self._linked_tracker_id = linked_tracker_id
        self._name = name
        self._created_at = created_at
        self._updated_at = updated_at
        self._mac_address = mac_address
        self._battery_level = battery_level
        self._last_battery_level_update = last_battery_level_update
        self._sleep_delay = sleep_delay
        self._is_updated = is_updated
        self._power = power


    @property
    def linked_tracker_id(self):
        """ linked_tracker_id property """
        return self._linked_tracker_id
    
    @linked_tracker_id.setter
    def linked_tracker_id(self, linked_tracker_id):
        """ linked_tracker_id setter """
        self._linked_tracker_id = linked_tracker_id

    @property
    def beacon_id(self):
        """beacon_id property"""
        return self._beacon_id

    @property
    def name(self):
        """name property"""
        return self._name

    @property
    def created_at(self):
        """created_at property"""
        return self._created_at

    @property
    def updated_at(self):
        """updated_at property"""
        return self._updated_at

    @property
    def mac_address(self):
        """mac_address property"""
        return self._mac_address

    @property
    def battery_level(self):
        """battery_level property"""
        return self._battery_level

    @property
    def last_battery_level_update(self):
        """last_battery_level_update property"""
        return self._last_battery_level_update

    @property
    def sleep_delay(self):
        """sleep_delay property"""
        return self._sleep_delay

    @property
    def is_updated(self):
        """is_updated property"""
        return self._is_updated

    @property
    def power(self):
        """power property"""
        return self._power

    @classmethod
    def from_json(cls, json):
        """return new object from_json"""
        return GeoRideTrackerBeacon(
            json['id'],
            json['linked_tracker_id'],
            json['name'],
            json['createdAt'],
            json['updatedAt'],
            json['macAddress'],
            json['batteryLevel'],
            json['lastBatteryLevelUpdate'],
            json['sleepDelay'],
            json['isUpdated'],
            json['power'])
    
    def update_all_data(self, tracker_beacon):
        """update all data of the tracker beacon from a new object"""
        self._name = tracker_beacon.name
        self._created_at = tracker_beacon.created_at
        self._updated_at = tracker_beacon.updated_at
        self._mac_address = tracker_beacon.mac_address
        self._battery_level = tracker_beacon.battery_level
        self._last_battery_level_update = tracker_beacon.last_battery_level_update
        self._sleep_delay = tracker_beacon.sleep_delay
        self._is_updated = tracker_beacon.is_updated
        self._power = tracker_beacon.power