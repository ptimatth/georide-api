"""
Georide objects implementation
@author Matthieu DUVAL <matthieu@duval-dev.fr>
"""
import time
import logging
from . import JsonMgtMetaClass, GeoRideSubscription

_LOGGER = logging.getLogger(__name__)

class GeoRideTracker(metaclass=JsonMgtMetaClass): # pylint: disable=R0904,R0902
    """ Tracker position object representation """
    def __init__(self, tracker_id, tracker_name, device_button_action, device_button_delay, # pylint: disable= R0913, R0914, R0915
                 vibration_level, is_old_tracker, auto_lock_freezed_to, fixtime, role,
                 last_payment_date, gift_card_id, expires, activation_date, odometer, is_stolen,
                 is_crashed, crash_detection_disabled, speed, moving, position_id, latitude, 
                 longitude, altitude, locked_position_id, locked_latitude, locked_longitude,
                 is_locked, can_see_position, can_lock, can_unlock, can_share, can_unshare,
                 can_check_speed, can_see_statistics, can_send_broken_down_signal,
                 can_send_stolen_signal, status, subscription_id, external_battery_voltage,
                 internal_battery_voltage, timezone, is_second_gen, is_up_to_date,
                 subscription, version, gift_card_expires, gift_card_months, odometer_updated_at,
                 maintenance_mode_until, battery_updated_at, is_in_eco, is_calibrated, 
                 is_oldsubscription, software_version, has_beacon, has_outdated_beacons, ecall_activated,
                 ecall_crash_mode, assistance_theft_activated,model, business_model, has_theft_case_opened):
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
        self._subscription_id = subscription_id
        self._external_battery_voltage = external_battery_voltage
        self._internal_battery_voltage = internal_battery_voltage
        self._timezone = timezone
        self._is_second_gen = is_second_gen
        self._is_up_to_date = is_up_to_date
        self._subscription = subscription
        self._version = version
        self._gift_card_expires = gift_card_expires
        self._gift_card_months = gift_card_months
        self._odometer_updated_at = odometer_updated_at
        self._maintenance_mode_until = maintenance_mode_until
        self._battery_updated_at = battery_updated_at
        self._is_in_eco = is_in_eco
        self._is_calibrated = is_calibrated
        self._is_oldsubscription = is_oldsubscription
        self._software_version = software_version
        self._has_beacon = has_beacon
        self._has_outdated_beacons = has_outdated_beacons
        self._ecall_activated = ecall_activated
        self._ecall_crash_mode = ecall_crash_mode
        self._assistance_theft_activated = assistance_theft_activated
        self._model = model
        self._business_model = business_model
        self._has_theft_case_opened = has_theft_case_opened
        self._is_siren_on = False
        self._siren_last_on_date = time.time()


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

    @property
    def subscription_id(self):
        """subscription_id property"""
        return self._subscription_id

    @property
    def external_battery_voltage(self):
        """_external_battery_voltage property"""
        return self._external_battery_voltage

    @property
    def internal_battery_voltage(self):
        """internal_battery_voltage property"""
        return self._internal_battery_voltage

    @property
    def timezone(self):
        """timezone property"""
        return self._timezone

    @property
    def is_second_gen(self):
        """is_second_gen property"""
        return self._is_second_gen

    @property
    def is_up_to_date(self):
        """is_up_to_date property"""
        return self._is_up_to_date

    @property
    def subscription(self):
        """ subscription property """
        return self._subscription

    @property
    def version(self):
        """ version property """
        return self._version

    @property
    def gift_card_expires(self):
        """ gift_card_expires property """
        return self._gift_card_expires

    @property
    def gift_card_months(self):
        """ gift_card_months property """
        return self._gift_card_months

    @property
    def odometer_updated_at(self):
        """ odometer_updated_at property """
        return self._odometer_updated_at

    @property
    def maintenance_mode_until(self):
        """ maintenance_mode_until property """
        return self._maintenance_mode_until

    @property
    def battery_updated_at(self):
        """ battery_updated_at property """
        return self._battery_updated_at

    @property
    def is_in_eco(self):
        """ is_in_eco property """
        return self._is_in_eco
    
    @is_in_eco.setter
    def is_in_eco(self, is_in_eco):
        """ is_in_eco setter """
        self._is_in_eco = is_in_eco

    @property
    def is_siren_on(self):
        """ is_siren_on property """
        return self._is_siren_on
    
    @is_siren_on.setter
    def is_siren_on(self, is_siren_on):
        """ is_siren_on setter """
        if is_siren_on:
            self._siren_last_on_date = time.time()
        self._is_siren_on = is_siren_on

    @property
    def siren_last_on_date(self):
        """ siren_last_on_date property """
        return self._siren_last_on_date

    @property
    def is_calibrated(self):
        """ is_calibrated property """
        return self._is_calibrated

    @property
    def is_oldsubscription(self):
        """ is_oldsubscription property """
        return self._is_oldsubscription
        
    @property
    def software_version(self):
        """ software_version property """
        return self._software_version

    @property
    def has_beacon(self):
        """ has_beacon property """
        return self._has_beacon

    @property
    def has_outdated_beacons(self):
        """ has_outdated_beacons property """
        return self._has_outdated_beacons

    @property
    def ecall_activated(self):
        """ ecall_activated property """
        return self._ecall_activated

    @property
    def version(self):
        """ version property """
        return self._version

    @property
    def ecall_crash_mode(self):
        """ eCallCrashMode property """
        return self._ecall_crash_mode

    @property
    def assistance_theft_activated(self):
        """ assistanceTheftActivated property """
        return self._assistance_theft_activated

    @property
    def model(self):
        """ model property """
        return self._model

    @property
    def business_model(self):
        """ businessModel property """
        return self._business_model

    @property
    def has_theft_case_opened(self):
        """ hasTheftCaseOpened property """
        return self._has_theft_case_opened
    
        
    @classmethod
    def from_json(cls, json):
        """return new object fromjson"""
    
        return GeoRideTracker(
            json['trackerId'], # Mandatory
            json['trackerName'], # Mandatory
            cls.json_field_protect(json,'deviceButtonAction'),
            cls.json_field_protect(json,'deviceButtonDelay'),
            cls.json_field_protect(json,'vibrationLevel'),
            cls.json_field_protect(json,'isOldTracker', False),
            cls.json_field_protect(json,'autoLockFreezedTo'),
            cls.json_field_protect(json,'fixtime'),
            cls.json_field_protect(json,'role', "owner"),
            cls.json_field_protect(json,'lastPaymentDate', null),
            cls.json_field_protect(json,'giftCardId'),
            cls.json_field_protect(json,'expires'),
            cls.json_field_protect(json,'activationDate'),
            cls.json_field_protect(json,'odometer', False),
            cls.json_field_protect(json,'isStolen', False),
            cls.json_field_protect(json,'isCrashed', False),
            cls.json_field_protect(json,'crashDetectionDisabled'),
            cls.json_field_protect(json,'speed', 0), # Mandatory
            cls.json_field_protect(json,'moving', False),
            cls.json_field_protect(json,'positionId', -1),
            cls.json_field_protect(json,'latitude', 47.0),
            cls.json_field_protect(json,'longitude', -1.0),
            cls.json_field_protect(json,'altitude', 0),
            cls.json_field_protect(json,'lockedPositionId'),
            cls.json_field_protect(json,'lockedLatitude'),
            cls.json_field_protect(json,'lockedLongitude'),
            cls.json_field_protect(json,'isLocked', False),
            cls.json_field_protect(json,'canSeePosition', False),
            cls.json_field_protect(json,'canLock', False),
            cls.json_field_protect(json,'canUnlock', False),
            cls.json_field_protect(json,'canShare', False),
            cls.json_field_protect(json,'canUnshare', False),
            cls.json_field_protect(json,'canCheckSpeed', False),
            cls.json_field_protect(json,'canSeeStatistics', False),
            cls.json_field_protect(json,'canSendBrokenDownSignal', False),
            cls.json_field_protect(json,'canSendStolenSignal', False),
            cls.json_field_protect(json,'status', 'unknown'),
            cls.json_field_protect(json,'subscriptionId', -1),
            cls.json_field_protect(json,'externalBatteryVoltage', -1.0),
            cls.json_field_protect(json,'internalBatteryVoltage', -1.0),
            cls.json_field_protect(json,'timezone', "Europe/Paris"),
            cls.json_field_protect(json,'isSecondGen', False),
            cls.json_field_protect(json,'isUpToDate', False),
            GeoRideSubscription.from_json(json['subscription']) if cls.json_field_protect(json,'subscription') is not None else None,
            cls.json_field_protect(json,'version', 1),
            cls.json_field_protect(json,'giftCardExpires'),
            cls.json_field_protect(json,'giftCardMonths'),
            cls.json_field_protect(json,'odometerUpdatedAt'),
            cls.json_field_protect(json,'maintenanceModeUntil'),
            cls.json_field_protect(json,'batteryUpdatedAt'),
            cls.json_field_protect(json,'isInEco', False),
            cls.json_field_protect(json,'isCalibrated', True),
            cls.json_field_protect(json,'isOldSubscription', True),
            cls.json_field_protect(json,'softwareVersion', 1),
            cls.json_field_protect(json,'hasBeacon', False),
            cls.json_field_protect(json,'hasOutdatedBeacons', False),
            cls.json_field_protect(json,'eCallActivated', False),
            cls.json_field_protect(json,'eCallCrashMode'),
            cls.json_field_protect(json,'assistanceTheftActivated'),
            cls.json_field_protect(json,'model'),
            cls.json_field_protect(json,'businessModel'),
            cls.json_field_protect(json,'hasTheftCaseOpened'),
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
        self._subscription_id = tracker.subscription_id
        self._external_battery_voltage = tracker.external_battery_voltage
        self._internal_battery_voltage = tracker.internal_battery_voltage
        self._timezone = tracker.timezone
        self._is_second_gen = tracker.is_second_gen
        self._is_up_to_date = tracker.is_up_to_date
        self._subscription = tracker.subscription
        self._version = tracker.version
        self._gift_card_expires = tracker.gift_card_expires
        self._gift_card_months = tracker.gift_card_months
        self._odometer_updated_at = tracker.odometer_updated_at
        self._maintenance_mode_until = tracker.maintenance_mode_until
        self._battery_updated_at = tracker.battery_updated_at
        self._is_in_eco = tracker.is_in_eco
        self._is_calibrated = tracker.is_calibrated
        self._is_oldsubscription = tracker.is_oldsubscription
        self._software_version = tracker.software_version
        self._has_beacon = tracker.has_beacon
        self._has_outdated_beacons = tracker.has_outdated_beacons
        self._ecall_activated = tracker.ecall_activated
        self._ecall_crash_mode =  tracker.ecall_crash_mode
        self._assistance_theft_activated =  tracker.assistance_theft_activated
        self._model =  tracker.model
        self._business_model =  tracker.business_model
        self._has_theft_case_opened =  tracker.has_theft_case_opened
