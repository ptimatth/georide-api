""" Example georideapilib code """
import logging.config
import time
import datetime
logging.config.fileConfig('logging.conf')
from georideapilib.objects import GeoRideAccount
import georideapilib.api as GeoRideApi
from georideapilib.socket import GeoRideSocket

from threading import Thread

_LOGGER = logging.getLogger('example')

DATE_START="2019-10-10"
DATE_END="2019-10-24"

def example():
    """ simple example function """
    # token = "<your_token>"# pylint: disable=C0301
    # account = GeoRideAccount(0, "<your_email>", False, token)

    
    account = GeoRideApi.get_authorisation_token("<your_email>", "<your_password>")
    print("token 1: ", account.auth_token)
    _LOGGER.info("token 1: %s", account.auth_token)
    # pylint: disable=W0105

    def locked_locked(data):
        _LOGGER.info("Lock received")

    def refresh_tracker():
        _LOGGER.info("Refresh tracker recieved")

    def connect_socket(account):
        socket = GeoRideSocket()
        socket.subscribe_locked(locked_locked)
        socket.subscribe_refresh_tracker(refresh_tracker)
        socket.init()
        socket.connect(account.auth_token)
        time.sleep(10)
        socket.disconnect()

    thread = Thread(target=connect_socket, args=[account])
    thread.start()
  
    """
    account.auth_token = GeoRideApi.renewToken(account.auth_token)
    print("token 2: ", account.auth_token) 
    """ # pylint: disable=W0105

    user = GeoRideApi.get_user(account.auth_token)
    _LOGGER.info("User: %s", user.first_name)

    trackers = GeoRideApi.get_trackers(account.auth_token)
    tracker = trackers[0]
    _LOGGER.info("Tracker name: %s", tracker.tracker_name)

    trips = GeoRideApi.get_trips(account.auth_token, tracker.tracker_id, DATE_START, DATE_END)
    if len(trips) < 1:
        _LOGGER.info("No trip found for tracker name: %s between: %s and %s", tracker.tracker_name,  DATE_START, DATE_END)
    else:
        trip = trips[0]
        trip_date = datetime.datetime.strptime("2019-10-10T06:45:34.000Z", '%Y-%m-%dT%H:%M:%S.%fZ')
        _LOGGER.info("Trip date: %s, from: %s, to: %s", trip_date, trip.nice_start_address,
                    trip.nice_end_address)

    positions = GeoRideApi.get_positions(account.auth_token, tracker.tracker_id,
                                         DATE_START, DATE_END)
    if len(positions) < 1:
        _LOGGER.info("No positions found for tracker name: %s between: %s and %s", tracker.tracker_name,  DATE_START, DATE_END)
    else:
        position = positions[0]
        _LOGGER.info("Position speed: %s, lon: %s, lat: %s", position.speed, position.longitude,
                    position.latitude)

    trip_shared = GeoRideApi.share_a_trip_by_date(account.auth_token, tracker.tracker_id,
                                                  DATE_START, DATE_END)
    _LOGGER.info("tripShared url: %s, id: %s", trip_shared.url, trip_shared.share_id)

    time.sleep(10)
    have_been_locked = GeoRideApi.lock_tracker(account.auth_token, tracker.tracker_id)
    _LOGGER.info("Tracker have been locked: %s", have_been_locked)

    time.sleep(10)
    have_been_unlocked = GeoRideApi.unlock_tracker(account.auth_token, tracker.tracker_id)
    _LOGGER.info("Tracker have been unlocked: %s", have_been_unlocked)

    time.sleep(10)
    is_locked = GeoRideApi.toogle_lock_tracker(account.auth_token, tracker.tracker_id)
    _LOGGER.info("Tracker is locked: %s", is_locked)

    time.sleep(10)
    trackers = GeoRideApi.get_trackers(account.auth_token)
    tracker = trackers[0]
    _LOGGER.info("Tracker name: %s is locked: %s", tracker.tracker_name, tracker.is_locked)

    if tracker.version >= 3:
        _LOGGER.info("Congrat for your new gen GeoRide \o/")

        # Have been commented for your neighbor ;)
        # time.sleep(10)
        # have_been_siren_turned_on = GeoRideApi.change_tracker_siren_state(account.auth_token, tracker.tracker_id, True)
        # _LOGGER.info("Tracker siren is on: %s", have_been_siren_turned_on)

        # time.sleep(5)
        # have_been_siren_turned_off = GeoRideApi.change_tracker_siren_state(account.auth_token, tracker.tracker_id, False)
        # _LOGGER.info("Tracker siren is off: %s", have_been_siren_turned_off)

        time.sleep(10)
        changed_to_eco_mode = GeoRideApi.change_tracker_eco_mode_state(account.auth_token, tracker.tracker_id, True)
        _LOGGER.info("Tracker eco mode is on: %s", changed_to_eco_mode)

        time.sleep(5)
        changed_to_normal_mode = GeoRideApi.change_tracker_eco_mode_state(account.auth_token, tracker.tracker_id, False)
        _LOGGER.info("Tracker eco mode is off: %s", changed_to_normal_mode)
        
        tracker_beacon = GeoRideApi.get_tracker_beacon(account.auth_token, tracker.tracker_id)
        _LOGGER.info("Your tracker beacon state: %s", tracker_beacon)

        #you can also shutdown your tracker with shutdown_tracker(<token>, tracker_id) but i d'on give you an example.
    else:
        _LOGGER.info("You are from the first wave ;)")


    """
    GeorideApi.revokeToken(account.auth_token)
    """ # pylint: disable=W0105
example()
