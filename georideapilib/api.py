"""
Georide api lib
@author Matthieu DUVAL <matthieu@duval-dev.fr>
"""

import json
import logging
import requests

from georideapilib.objects import (
    GeoRideTracker, 
    GeoRideAccount, 
    GeoRideUser,  
    GeoRideTrackerTrip,  
    GeoRideTrackerPosition, 
    GeoRideSharedTrip
)

from georideapilib.exception import (
    LoginException,
    SeverException,
    UnauthorizedException
)

GEORIDE_API_HOST = "https://api.georide.fr"
GEORIDE_API_ENDPOINT_LOGIN = "/user/login"
GEORIDE_API_ENDPOINT_NEW_TOKEN = "/user/new-token"
GEORIDE_API_ENDPOINT_LOGOUT = "/user/logout"
GEORIDE_API_ENDPOINT_USER = "/user"
GEORIDE_API_ENDPOINT_TRAKERS = "/user/trackers"
GEORIDE_API_ENDPOINT_TRIPS = "/tracker/:trackerId/trips"
GEORIDE_API_ENDPOINT_LOCK = "/tracker/:trackerId/lock"
GEORIDE_API_ENDPOINT_UNLOCK = "/tracker/:trackerId/unlock"
GEORIDE_API_ENDPOINT_TOGGLE_LOCK = "/tracker/:trackerId/toggleLock"
GEORIDE_API_ENDPOINT_POSITIONS = "/tracker/:trackerId/trips/positions"
GEORIDE_API_ENDPOINT_TRIP_SHARE = "/tracker/:trackerId/share/trip"

_SESSION = requests.Session()
_LOGGER = logging.getLogger(__name__)

def get_authorisation_token(email, password):
    """ return an authorization token or no"""
    data = {"email": email, "password": password}
    encoded_data = json.dumps(data).encode('utf-8')

    response = _SESSION.post( 
        GEORIDE_API_HOST + GEORIDE_API_ENDPOINT_LOGIN,
        data=encoded_data,
        headers={'Content-Type': 'application/json'})
    
    if response.status_code == 200:
        _LOGGER.debug("Login success")
        response_data = response.json()
        account = GeoRideAccount.from_json(response_data)
    elif response.status_code == 403:
        _LOGGER.warning("Login failed")
        raise LoginException(get_authorisation_token, "Login failed")
    else:
        _LOGGER.error("Georide login, http error code: %s", response.status_code)
        raise SeverException(get_authorisation_token, 
                             "Georide login, http error code: {}".format(response.status_code))
    return account


def renew_token(token):
    """ renew the authorization token """
    headers = {"Authorization": "Bearer " + token}
    response = _SESSION.get(
        GEORIDE_API_HOST + GEORIDE_API_ENDPOINT_NEW_TOKEN,
        headers=headers)
    if response.status_code == 200:
        _LOGGER.debug("Token updated")
        response_data = response.json()
        new_token = response_data['authToken']
    elif response.status_code == 401:
        _LOGGER.warnning("Renew token refused")
        raise UnauthorizedException(renew_token, "Renew token refused")
    else:
        _LOGGER.error("Georide login, http error code: %s", response.status_code)
        raise SeverException(renew_token, 
                             "Georide login, http error code: {}".format(response.status_code))
    return new_token

def revoke_token(token):
    """ invalidate the authorization token """
    headers = {"Authorization": "Bearer " + token}
    response = _SESSION.post(
        GEORIDE_API_HOST + GEORIDE_API_ENDPOINT_LOGOUT,
        headers=headers)
    if response.status_code == 401:
        _LOGGER.warnning("Token allready revoked")
        raise UnauthorizedException(revoke_token, "Token allready revoked")
    if response.status_code == 401:
        _LOGGER.warnning("Token allready revoked")
        return False
    return True


def get_user(token):
    """ get the georide user info """
    headers = {"Authorization": "Bearer " + token}
    response = _SESSION.get(
        GEORIDE_API_HOST + GEORIDE_API_ENDPOINT_USER,
        headers=headers)
    response_data = response.json()
    _LOGGER.debug(response_data)
    account = GeoRideUser.from_json(response_data)
    return account  

def get_trackers(token):
    """ get user trackers """

    headers = {"Authorization": "Bearer " + token}
    response = _SESSION.get(
        GEORIDE_API_HOST + GEORIDE_API_ENDPOINT_TRAKERS,
        headers=headers)

    response_data = response.json()
    trackers = []
    for json_tracker in response_data:
        _LOGGER.debug(json_tracker)
        trackers.append(GeoRideTracker.from_json(json_tracker))
    return trackers


def get_trips(token, tracker_id, from_date, to_date):
    """ return all trips between two dates """
    headers = {"Authorization": "Bearer " + token}
    response = _SESSION.get(
        GEORIDE_API_HOST + GEORIDE_API_ENDPOINT_TRIPS.replace(':trackerId', str(tracker_id)),
        params={'from': from_date, 'to': to_date},
        headers=headers)

    response_data = response.json()
    trips = []
    for json_trip in response_data:
        trips.append(GeoRideTrackerTrip.from_json(json_trip))
    return trips

def get_positions(token, tracker_id, from_date, to_date):
    """ return all trips between two dates """
    headers = {"Authorization": "Bearer " + token}
    response = _SESSION.get(
        GEORIDE_API_HOST + GEORIDE_API_ENDPOINT_POSITIONS.replace(':trackerId', str(tracker_id)),
        params={'from': from_date, 'to': to_date},
        headers=headers)

    response_data = response.json()
    positions = []
    for json_position in response_data:
        positions.append(GeoRideTrackerPosition.from_json(json_position))
    return positions

def share_a_trip_by_trip_id(token, tracker_id, trip_id):
    """ share trip by trip id """
    return _share_a_trip(token, tracker_id, trip_id=trip_id)

def share_a_trip_by_date(token, tracker_id, from_date, to_date):
    """ share trips between two dates """
    return _share_a_trip(token, tracker_id, from_date=from_date, to_date=to_date)

def share_a_trip_by_trip_merge_id(token, tracker_id, trip_merged_id):
    """ share trip by trip merged id """
    return _share_a_trip(token, tracker_id, trip_merged_id=trip_merged_id)

def _share_a_trip(token, tracker_id, trip_id=None, from_date=None, # pylint: disable= R0913
                  to_date=None, trip_merged_id=None): 
    """ share trip by trib_id or between two dates or trip_merged_id """
    data = None
    if trip_id is not None:
        data = {"tripId": trip_id}
    elif from_date is not None and to_date is not None:
        data = {"from": from_date, "to": to_date}
    elif trip_merged_id is not None:
        data = {"tripMergedId": trip_merged_id}

    encoded_data = json.dumps(data).encode('utf-8')

    headers = {
        "Authorization": "Bearer " + token,
        'Content-Type': 'application/json'
    }
    response = _SESSION.post(
        GEORIDE_API_HOST + GEORIDE_API_ENDPOINT_TRIP_SHARE.replace(':trackerId', str(tracker_id)),
        data=encoded_data,
        headers=headers)

    response_data = response.json()
    return GeoRideSharedTrip.from_json(response_data)

def lock_tracker(token, tracker_id):
    """ used to lock a tracker """
    headers = {"Authorization": "Bearer " + token}
    response = _SESSION.post(
        GEORIDE_API_HOST + GEORIDE_API_ENDPOINT_LOCK.replace(':trackerId', str(tracker_id)),
        headers=headers)
    if response.status_code != 204:
        return False
    return True

def unlock_tracker(token, tracker_id):
    """ used to unlock a tracker """
    headers = {"Authorization": "Bearer " + token}
    response = _SESSION.post(
        GEORIDE_API_HOST + GEORIDE_API_ENDPOINT_UNLOCK.replace(':trackerId', str(tracker_id)),
        headers=headers)
    if response.status_code != 204:
        return False
    return True

def toogle_lock_tracker(token, tracker_id):
    """ used to toggle lock a tracker """
    headers = {"Authorization": "Bearer " + token}
    response = _SESSION.post(
        GEORIDE_API_HOST + GEORIDE_API_ENDPOINT_TOGGLE_LOCK.replace(':trackerId', str(tracker_id)),
        headers=headers)
    response_data = response.json()
    return response_data['locked']

if __name__ == '__main__':
    print("Not a main module")
