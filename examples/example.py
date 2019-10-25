""" Example georideapilib code """


import time
import datetime

from georideapilib.objects import GeorideAccount
import georideapilib.api as GeorideApi


def example():
    """ simple example function """
    token = "<your_token>"# pylint: disable=C0301
    account = GeorideAccount(0, "<your_email>", False, token)

    """
    GeorideApi.getAuthorisationToken("<your_email>", "<your_password>")
    print("token 1: ", account.auth_token)
    """ # pylint: disable=W0105


    """
    account.auth_token = GeorideApi.renewToken(account.auth_token)
    print("token 2: ", account.auth_token) 
    """ # pylint: disable=W0105

    user = GeorideApi.get_user(account.auth_token)
    print("User: ", user.first_name)

    trackers = GeorideApi.get_trackers(account.auth_token)
    tracker = trackers[0]
    print("Tracker name: ", tracker.tracker_name)

    trips = GeorideApi.get_trips(account.auth_token, tracker.tracker_id, "2019-10-10", "2019-10-24")
    trip = trips[0]
    trip_date = datetime.datetime.strptime("2019-10-10T06:45:34.000Z", '%Y-%m-%dT%H:%M:%S.%fZ')
    print("Trip date: {}, from: {}, to: {}".format(trip_date, trip.nice_start_address,
                                                   trip.nice_end_address))

    positions = GeorideApi.get_positions(account.auth_token, tracker.tracker_id,
                                         "2019-10-10", "2019-10-24")
    position = positions[0]
    print("Position speed: {}, lon: {}, lat: {}".format(position.speed, position.longitude,
                                                        position.latitude))


    trip_shared = GeorideApi.share_a_trip_by_date(account.auth_token, tracker.tracker_id,
                                                  "2019-10-10", "2019-10-24")
    print("tripShared url: {}, id: {}".format(trip_shared.url, trip_shared.share_id))

    time.sleep(10)
    have_been_locked = GeorideApi.lock_tracker(account.auth_token, tracker.tracker_id)
    print("Tracker have been locked: ", have_been_locked)

    time.sleep(10)
    have_been_unlocked = GeorideApi.unlock_tracker(account.auth_token, tracker.tracker_id)
    print("Tracker have been unlocked: ", have_been_unlocked)

    time.sleep(10)
    is_locked = GeorideApi.toogle_lock_tracker(account.auth_token, tracker.tracker_id)
    print("Tracker is locked: ", is_locked)

    time.sleep(10)
    trackers = GeorideApi.get_trackers(account.auth_token)
    tracker = trackers[0]
    print("Tracker name: ", tracker.tracker_name, " is locked: ", tracker.is_locked)

    """
    GeorideApi.revokeToken(account.auth_token)
    """ # pylint: disable=W0105

example()