""" Example georideapilib code """


import time
import datetime

logging.config.fileConfig('logging.conf')
from georideapilib.objects import GeorideAccount
import georideapilib.api as GeorideApi
from georideapilib.socket import GeorideSocket

from threading import Thread

_LOGGER = logging.getLogger('example')


def example():
    """ simple example function """
    # token = "<your_token>"# pylint: disable=C0301
    # account = GeorideAccount(0, "<your_email>", False, token)

    
    account = GeorideApi.get_authorisation_token("<your_email>", "<your_password>")
    print("token 1: ", account.auth_token)
    _LOGGER.info("token 1: %s", account.auth_token)
    # pylint: disable=W0105

    def locked_locked(data):
        _LOGGER.info("Locke received")


    def connect_socket(account):
        socket = GeorideSocket()
        socket.subscribe_locked(locked_locked)
        socket.init()
        socket.connect(account.auth_token)
        time.sleep(10)
        socket.disconnect()

    thread = Thread(target=connect_socket, args=(account))
    thread.start()
  
    """
    account.auth_token = GeorideApi.renewToken(account.auth_token)
    print("token 2: ", account.auth_token) 
    """ # pylint: disable=W0105

    user = GeorideApi.get_user(account.auth_token)
    _LOGGER.info("User: %s", user.first_name)

    trackers = GeorideApi.get_trackers(account.auth_token)
    tracker = trackers[0]
    _LOGGER.info("Tracker name: %s", tracker.tracker_name)

    trips = GeorideApi.get_trips(account.auth_token, tracker.tracker_id, "2019-10-10", "2019-10-24")
    trip = trips[0]
    trip_date = datetime.datetime.strptime("2019-10-10T06:45:34.000Z", '%Y-%m-%dT%H:%M:%S.%fZ')
    _LOGGER.info("Trip date: %s, from: %s, to: %s", trip_date, trip.nice_start_address,
                 trip.nice_end_address)

    positions = GeorideApi.get_positions(account.auth_token, tracker.tracker_id,
                                         "2019-10-10", "2019-10-24")
    position = positions[0]
    _LOGGER.info("Position speed: %s, lon: %s, lat: %s", position.speed, position.longitude,
                 position.latitude)


    trip_shared = GeorideApi.share_a_trip_by_date(account.auth_token, tracker.tracker_id,
                                                  "2019-10-10", "2019-10-24")
    _LOGGER.info("tripShared url: %s, id: %s", trip_shared.url, trip_shared.share_id)

    time.sleep(10)
    have_been_locked = GeorideApi.lock_tracker(account.auth_token, tracker.tracker_id)
    _LOGGER.info("Tracker have been locked: %s", have_been_locked)

    time.sleep(10)
    have_been_unlocked = GeorideApi.unlock_tracker(account.auth_token, tracker.tracker_id)
    _LOGGER.info("Tracker have been unlocked: %s", have_been_unlocked)

    time.sleep(10)
    is_locked = GeorideApi.toogle_lock_tracker(account.auth_token, tracker.tracker_id)
    _LOGGER.info("Tracker is locked: %s", is_locked)

    time.sleep(10)
    trackers = GeorideApi.get_trackers(account.auth_token)
    tracker = trackers[0]
    _LOGGER.info("Tracker name: %s is locked: %s", tracker.tracker_name, tracker.is_locked)




    """
    GeorideApi.revokeToken(account.auth_token)
    """ # pylint: disable=W0105
example()
