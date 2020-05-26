""" GeoRide socket-io implementation """
import logging
import socketio

from georideapilib.api import GEORIDE_API_HOST

_LOGGER = logging.getLogger(__name__)

sio = socketio.Client(reconnection=True) # pylint: disable=C0103

@sio.on('connect')
def on_connect():
    """ event: connected """
    _LOGGER.debug('GeoRide socket connected')

@sio.on('disconnect')
def on_disconnect():
    """ event: disconnected """
    _LOGGER.debug('GeoRide socket disconnected')


class GeoRideSocket():
    """docstring for GeoRideSocket"""
    def __init__(self):
        self._on_message_callback = None
        self._on_device_callback = None
        self._on_position_callback = None
        self._on_alarm_callback = None
        self._on_refresh_tracker_callback = None
        self._on_locked_callback = None
        self._initialised = False


    def subscribe_on_message(self, callback_function):
        """event: tells you authentication informations."""
        self._on_message_callback = callback_function

    def subscribe_device(self, callback_function):
        """event: tells you when a device is added to the account."""
        self._on_device_callback = callback_function

    def subscribe_position(self, callback_function):
        """event: tells you when a device sent a position."""
        self._on_position_callback = callback_function

    def subscribe_alarm(self, callback_function):
        """event: tells you when a device trigger an alarm."""
        self._on_alarm_callback = callback_function

    def subscribe_refresh_tracker(self, callback_function):
        """event: tells you when you need to refresh your list of trackers"""
        self._on_refresh_tracker_callback = callback_function

    def subscribe_locked(self, callback_function):
        """event: tells you when a device has been locked or unlocked."""
        self._on_locked_callback = callback_function


    def init(self):
        """init the context"""
        @sio.on('message')
        def on_message(data):
            """ on_message """
            _LOGGER.debug('Message received: %s', data)
            if self._on_message_callback is not None:
                self._on_message_callback(data)
        
        @sio.on('device')
        def on_device(data):
            """ on_device """
            _LOGGER.debug('Device received: %s', data)
            if self._on_device_callback is not None:
                self._on_device_callback(data)
        
        @sio.on('position')
        def on_position(data):
            """ on_position """
            _LOGGER.debug('Position received:%s', data)
            if self._on_position_callback is not None:
                self._on_position_callback(data)

        @sio.on('alarm')
        def on_alarm(data):
            """ on_alarm """
            _LOGGER.debug('Alarm received: %s', data)
            if self._on_alarm_callback is not None:
                self._on_alarm_callback(data)
            
        @sio.on('refreshTrackersInstruction')
        def on_refresh_tracker():
            """ on_refresh_tracker """
            _LOGGER.debug('Refresh tracker received')
            if self._on_refresh_tracker_callback is not None:
                self._on_refresh_tracker_callback()

        @sio.on('lockedPosition')
        def on_locked(data):
            """ on_locked """
            _LOGGER.debug('Locked received: %s', data)
            if self._on_locked_callback is not None:
                self._on_locked_callback(data)        
        self._initialised = True

    def connect(self, auth_token):
        """ connect to the georide socket"""
        if self._initialised is not False:
            sio.connect(GEORIDE_API_HOST, headers={'token': auth_token})
            sio.wait()
        else:
            _LOGGER.error("Please call init() before")
        
    def disconnect(self):
        """disconnect from the georide socket"""
        sio.disconnect()


#TODO: remove in v0.8.0
class GeorideSocket(GeoRideSocket):
    """ Trip object representation """
    def __init_subclass__(cls, **kwargs):
        """Print deprecation warning."""
        super().__init_subclass__(**kwargs)
        _LOGGER.warning(
            "GeorideSocket is deprecated, modify %s to use GeoRideSocket",
            cls.__name__,
        )
    def __init__(self, *argv):
        """Print deprecation warning."""
        super().__init__(*argv)
        _LOGGER.warning("GeorideSocket is deprecated, modify your code to use GeoRideSocket")