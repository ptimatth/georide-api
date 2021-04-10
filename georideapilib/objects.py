"""
Georide objects implementation
@author Matthieu DUVAL <matthieu@duval-dev.fr>
"""

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

class GeoRideTracker: # pylint: disable=R0904,R0902
    """ Tracker position object representation """
    def __init__(self, tracker_id, tracker_name, device_button_action, device_button_delay, # pylint: disable= R0913, R0914, R0915
                 vibration_level, is_old_tracker, auto_lock_freezed_to, fixtime, role,
                 last_payment_date, gift_card_id, expires, activation_date, odometer, is_stolen,
                 is_crashed, crash_detection_disabled, speed, moving, position_id, latitude, 
                 longitude, altitude, locked_position_id, locked_latitude, locked_longitude,
                 is_locked, can_see_position, can_lock, can_unlock, can_share, can_unshare,
                 can_check_speed, can_see_statistics, can_send_broken_down_signal,
                 can_send_stolen_signal, status):
        self._tracker_id = tracker_id
        self._tracker_name = tracker_name
        self._device_button_action = device_button_action
        self._device_button_delay = device_button_delay
        self._vibration_level = vibration_level
        self._is_old_tracker = is_old_tracker
        self._position_id = position_id
        self._fixtime = fixtime
        self._latitude = latitude
        self._longitude = longitude
        self._altitude = altitude
        self._locked_position_id = locked_position_id
        self._locked_latitude = locked_latitude
        self._locked_longitude = locked_longitude
        self._role = role
        self._last_payment_date = last_payment_date
        self._gift_card_id = gift_card_id 
        self._expires = expires
        self._activation_date = activation_date
        self._odometer = odometer
        self._is_locked = is_locked
        self._is_stolen = is_stolen
        self._is_crashed = is_crashed
        self._crash_detection_disabled = crash_detection_disabled
        self._speed = speed
        self._moving = moving
        self._can_see_position = can_see_position
        self._can_lock = can_lock
        self._can_unlock = can_unlock
        self._can_share = can_share
        self._can_unshare = can_unshare
        self._can_check_speed = can_check_speed
        self._can_see_statistics = can_see_statistics
        self._can_send_broken_down_signal = can_send_broken_down_signal
        self._can_send_stolen_signal = can_send_stolen_signal
        self._status = status
        self._auto_lock_freezed_to = auto_lock_freezed_to

    @property
    def tracker_id(self):
        """ tracker_id """
        return self._tracker_id
    
    @property
    def tracker_name(self):
        """ tracker_name """
        return self._tracker_name
    
    @property
    def device_button_action(self):
        """ device_button_action """
        return self._device_button_action
    
    @property
    def device_button_delay(self):
        """ device_button_delay """
        return self._device_button_delay
    
    @property
    def vibration_level(self):
        """ vibration_level """
        return self._vibration_level
    
    @property
    def is_old_tracker(self):
        """ is_old_tracker """
        return self._is_old_tracker
    
    @property
    def auto_lock_freezed_to(self):
        """ auto_lock_freezed_to """
        return self._auto_lock_freezed_to
    
    @property
    def fixtime(self):
        """ fixtime """
        return self._fixtime
    
    @fixtime.setter
    def fixtime(self, fixtime):
        """ fixtime """
        self._fixtime = fixtime

    @property
    def role(self):
        """ role """
        return self._role
    
    @property
    def last_payment_date(self):
        """ last_payment_date """
        return self._last_payment_date
    
    @property
    def gift_card_id(self):
        """ gift_card_id """
        return self._gift_card_id
    
    @property
    def expires(self):
        """ expires """
        return self._expires
    
    @property
    def activation_date(self):
        """ activation_date """
        return self._activation_date
    
    @property
    def odometer(self):
        """ odometer """
        return self._odometer
    
    @property
    def is_stolen(self):
        """ is_stolen """
        return self._is_stolen

    @is_stolen.setter
    def is_stolen(self, is_stolen):
        """ is_stolen setter"""
        self._is_stolen = is_stolen
    
    @property
    def is_crashed(self):
        """ is_crashed """
        return self._is_crashed
    
    @is_crashed.setter
    def is_crashed(self, is_crashed):
        """ is_crashed setter"""
        self._is_crashed = is_crashed

    @property
    def crash_detection_disabled(self):
        """ crash_detection_disabled """
        return self._crash_detection_disabled
    
    @property
    def speed(self):
        """ speed """
        return self._speed
    
    @speed.setter
    def speed(self, speed):
        """ speed """
        self._speed = speed

    @property
    def moving(self):
        """ moving """
        return self._moving
    
    @moving.setter
    def moving(self, moving):
        """ moving """
        self._moving = moving

    @property
    def position_id(self):
        """ position_id """
        return self._position_id
    
    @property
    def latitude(self):
        """ latitude """
        return self._latitude
    
    @latitude.setter
    def latitude(self, latitude):
        """ latitude """
        self._latitude = latitude

    @property
    def longitude(self):
        """ longitude """
        return self._longitude
    
    @longitude.setter
    def longitude(self, longitude):
        """ longitude """
        self._longitude = longitude
    
    @property
    def altitude(self):
        """ altitude """
        return self._altitude
    
    @property
    def locked_position_id(self):
        """ locked_position_id """
        return self._locked_position_id
    
    @property
    def locked_latitude(self):
        """ locked_latitude """
        return self._locked_latitude
    
    @locked_latitude.setter
    def locked_latitude(self, locked_latitude):
        """ locked_latitude """
        self._locked_latitude = locked_latitude

    @property
    def locked_longitude(self):
        """ locked_longitude """
        return self._locked_longitude

    @locked_longitude.setter
    def locked_longitude(self, locked_longitude):
        """ locked_longitude """
        self._locked_longitude = locked_longitude

    @property
    def is_locked(self):
        """ is_locked """
        return self._is_locked
    
    @is_locked.setter
    def is_locked(self, is_locked):
        """ is_locked """
        self._is_locked = is_locked

    @property
    def can_see_position(self):
        """ can_see_position """
        return self._can_see_position
    
    @property
    def can_lock(self):
        """ can_lock """
        return self._can_lock
    
    @property
    def can_unlock(self):
        """ can_unlock """
        return self._can_unlock
    
    @property
    def can_share(self):
        """ can_share """
        return self._can_share
    
    @property
    def can_unshare(self):
        """ can_unshare """
        return self._can_unshare
    
    @property
    def can_check_speed(self):
        """ can_check_speed """
        return self._can_check_speed
    
    @property
    def can_see_statistics(self):
        """ can_see_statistics """
        return self._can_see_statistics
    
    @property
    def can_send_broken_down_signal(self):
        """ can_send_broken_down_signal """
        return self._can_send_broken_down_signal
    
    @property
    def can_send_stolen_signal(self):
        """ can_send_stolen_signal """
        return self._can_send_stolen_signal
    
    @property
    def status(self):
        """ status """
        return self._status

    @status.setter
    def status(self, status):
        """ status """
        self._status = status

    @staticmethod
    def from_json(json):
        """return new object fromjson"""
        return GeoRideTracker(
            json['trackerId'],
            json['trackerName'],
            json['deviceButtonAction'],
            json['deviceButtonDelay'],
            json['vibrationLevel'],
            json['isOldTracker'],
            json['autoLockFreezedTo'],
            json['fixtime'],
            json['role'],
            json['lastPaymentDate'],
            json['giftCardId'],
            json['expires'],
            json['activationDate'],
            json['odometer'],
            json['isStolen'],
            json['isCrashed'],
            json['crashDetectionDisabled'],
            json['speed'],
            json['moving'],
            json['positionId'],
            json['latitude'],
            json['longitude'],
            json['altitude'],
            json['lockedPositionId'],
            json['lockedLatitude'],
            json['lockedLongitude'],
            json['isLocked'],
            json['canSeePosition'],
            json['canLock'],
            json['canUnlock'],
            json['canShare'],
            json['canUnshare'],
            json['canCheckSpeed'],
            json['canSeeStatistics'],
            json['canSendBrokenDownSignal'],
            json['canSendStolenSignal'],
            json['status']
        )

    def update_all_data(self, tracker):
        """update all data of th tracker from anew object"""
        self._tracker_name = tracker.tracker_name
        self._device_button_action = tracker.device_button_action
        self._device_button_delay = tracker.device_button_delay
        self._vibration_level = tracker.vibration_level
        self._is_old_tracker = tracker.is_old_tracker
        self._position_id = tracker.position_id
        self._fixtime = tracker.fixtime
        self._latitude = tracker.latitude
        self._longitude = tracker.longitude
        self._altitude = tracker.altitude
        self._locked_position_id = tracker.locked_position_id
        self._locked_latitude = tracker.locked_latitude
        self._locked_longitude = tracker.locked_longitude
        self._role = tracker.role
        self._last_payment_date = tracker.last_payment_date
        self._gift_card_id = tracker.gift_card_id 
        self._expires = tracker.expires
        self._activation_date = tracker.activation_date
        self._odometer = tracker.odometer
        self._is_locked = tracker.is_locked
        self._is_stolen = tracker.is_stolen
        self._is_crashed = tracker.is_crashed
        self._crash_detection_disabled = tracker.crash_detection_disabled
        self._speed = tracker.speed
        self._moving = tracker.moving
        self._can_see_position = tracker.can_see_position
        self._can_lock = tracker.can_lock
        self._can_unlock = tracker.can_unlock
        self._can_share = tracker.can_share
        self._can_unshare = tracker.can_unshare
        self._can_check_speed = tracker.can_check_speed
        self._can_see_statistics = tracker.can_see_statistics
        self._can_send_broken_down_signal = tracker.can_send_broken_down_signal
        self._can_send_stolen_signal = tracker.can_send_stolen_signal
        self._status = tracker.status
        self._auto_lock_freezed_to = tracker.auto_lock_freezed_to

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

#TODO: remove in v0.8.0
class GeorideSharedTrip(GeoRideSharedTrip):
    """ Shared trip object representation """

    def __init_subclass__(cls, **kwargs):
        """Print deprecation warning."""
        super().__init_subclass__(**kwargs)
        _LOGGER.warning(
            "GeorideSharedTrip is deprecated, modify %s to use GeoRideSharedTrip",
            cls.__name__,
        )

    def __init__(self, *argv):
        """Print deprecation warning."""
        super().__init__(*argv)
        _LOGGER.warning("GeorideSharedTrip is deprecated, modify your code to use GeoRideSharedTrip")

class GeorideTrackerTrip(GeoRideTrackerTrip):
    """ Trip object representation """
    def __init_subclass__(cls, **kwargs):
        """Print deprecation warning."""
        super().__init_subclass__(**kwargs)
        _LOGGER.warning(
            "GeorideTrackerTrip is deprecated, modify %s to use GeoRideTrackerTrip",
            cls.__name__,
        )
    def __init__(self, *argv):
        """Print deprecation warning."""
        super().__init__(*argv)
        _LOGGER.warning("GeorideTrackerTrip is deprecated, modify your code to use GeoRideTrackerTrip")

class GeorideTrackerPosition(GeoRideTrackerPosition):
    """ Trip object representation """
    def __init_subclass__(cls, **kwargs):
        """Print deprecation warning."""
        super().__init_subclass__(**kwargs)
        _LOGGER.warning(
            "GeorideTrackerPosition is deprecated, modify %s to use GeoRideTrackerPosition",
            cls.__name__,
        )

    def __init__(self, *argv):
        """Print deprecation warning."""
        super().__init__(*argv)
        _LOGGER.warning("GeorideTrackerPosition is deprecated, modify your code to use GeoRideTrackerPosition")

class GeorideTracker(GeoRideTracker):
    """ Trip object representation """
    def __init_subclass__(cls, **kwargs):
        """Print deprecation warning."""
        super().__init_subclass__(**kwargs)
        _LOGGER.warning(
            "GeorideTracker is deprecated, modify %s to use GeoRideTracker",
            cls.__name__,
        )

    def __init__(self, *argv):
        """Print deprecation warning."""
        super().__init__(*argv)
        _LOGGER.warning("GeorideTracker is deprecated, modify your code to use GeoRideTracker")


class GeorideAccount(GeoRideAccount):
    """ Trip object representation """
    def __init_subclass__(cls, **kwargs):
        """Print deprecation warning."""
        super().__init_subclass__(**kwargs)
        _LOGGER.warning(
            "GeorideAccount is deprecated, modify %s to use GeoRideAccount",
            cls.__name__,
        )

    def __init__(self, *argv):
        """Print deprecation warning."""
        super().__init__(*argv)
        _LOGGER.warning("GeorideAccount is deprecated, modify your code to use GeoRideAccount")

class GeorideUser(GeoRideUser):
    """ Trip object representation """
    def __init_subclass__(cls, **kwargs):
        """Print deprecation warning."""
        super().__init_subclass__(**kwargs)
        _LOGGER.warning(
            "GeorideUser is deprecated, modify %s to use GeoRideUser",
            cls.__name__,
        )

    def __init__(self, *argv):
        """Print deprecation warning."""
        super().__init__(*argv)
        _LOGGER.warning("GeorideUser is deprecated, modify your code to use GeoRideUser")
