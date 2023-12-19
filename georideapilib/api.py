"""
Georide api lib
@author Matthieu DUVAL <matthieu@duval-dev.fr>
"""

import json
import logging

import requests

from georideapilib.exception import (
    LoginException,
    SeverException,
    UnauthorizedException
)
from georideapilib.objects import (
    GeoRideTracker,
    GeoRideAccount,
    GeoRideUser,
    GeoRideTrackerTrip,
    GeoRideTrackerPosition,
    GeoRideSharedTrip,
    GeoRideTrackerBeacon,
    GeoRideMaintenance
)

GEORIDE_API_HOST = "https://api.georide.com"
GEORIDE_SOCKET_HOST = "https://socket.georide.com"
GEORIDE_API_ENDPOINT_LOGIN = "/user/login"
GEORIDE_API_ENDPOINT_NEW_TOKEN = "/user/new-token"
GEORIDE_API_ENDPOINT_LOGOUT = "/user/logout"
GEORIDE_API_ENDPOINT_USER = "/user"
GEORIDE_API_ENDPOINT_TRACKERS = "/user/trackers"
GEORIDE_API_ENDPOINT_TRIPS = "/tracker/{trackerId}/trips"
GEORIDE_API_ENDPOINT_LOCK = "/tracker/{trackerId}/lock"
GEORIDE_API_ENDPOINT_TRACKER_BEACON = "/tracker/{trackerId}/beacon"
GEORIDE_API_ENDPOINT_UNLOCK = "/tracker/{trackerId}/unlock"
GEORIDE_API_ENDPOINT_TOGGLE_LOCK = "/tracker/{trackerId}/toggleLock"
GEORIDE_API_ENDPOINT_POSITIONS = "/tracker/{trackerId}/trips/positions"
GEORIDE_API_ENDPOINT_TRIP_SHARE = "/tracker/{trackerId}/share/trip"
GEORIDE_API_ENDPOINT_SHUTDOWN_TRACKER = "/tracker/{trackerId}/shutdown"
GEORIDE_API_ENDPOINT_TRACKER_ALARM_OFF = "/tracker/{trackerId}/sonor-alarm/off"
GEORIDE_API_ENDPOINT_TRACKER_ALARM_ON = "/tracker/{trackerId}/sonor-alarm/on"
GEORIDE_API_ENDPOINT_TRACKER_ECO_MODE_OFF = "/tracker/{trackerId}/eco-mode/off"
GEORIDE_API_ENDPOINT_TRACKER_ECO_MODE_ON = "/tracker/{trackerId}/eco-mode/on"
GEORIDE_API_ENDPOINT_TRACKER_DELETE_MAINTENANCE = "/tracker/{trackerId}/maintenance/{maintenanceId}"
GEORIDE_API_ENDPOINT_TRACKER_MAINTENANCE = "/tracker/{trackerId}/maintenance"

_SESSION = requests.Session()
_LOGGER = logging.getLogger(__name__)


def get_authorisation_token(email, password):
    """ return an authorization token or no"""
    data = {"email": email, "password": password}
    encoded_data = json.dumps(data).encode('utf-8')

    response = _send_request(
        "POST",
        GEORIDE_API_ENDPOINT_LOGIN,
        token=None,
        data=encoded_data,
    )

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
    response = _send_request(
        "GET",
        GEORIDE_API_ENDPOINT_NEW_TOKEN,
        token
    )
    if response.status_code == 200:
        _LOGGER.debug("Token updated")
        response_data = response.json()
        new_token = response_data['authToken']
    elif response.status_code == 401:
        _LOGGER.warning("Renew token refused")
        raise UnauthorizedException(renew_token, "Renew token refused")
    else:
        _LOGGER.error("Georide login, http error code: %s", response.status_code)
        raise SeverException(renew_token,
                             "Georide login, http error code: {}".format(response.status_code))
    return new_token


def revoke_token(token):
    """ invalidate the authorization token """
    response = _send_request(
        "POST",
        GEORIDE_API_ENDPOINT_LOGOUT,
        token
    )
    if response.status_code == 401:
        _LOGGER.warning("Token already revoked")
        raise UnauthorizedException(revoke_token, "Token allready revoked")
    if response.status_code == 403:
        _LOGGER.warning("Token already revoked")
        return False
    return True


def get_user(token):
    """ get the georide user info """
    response = _send_request(
        "GET",
        GEORIDE_API_ENDPOINT_USER,
        token
    )
    response_data = response.json()
    _LOGGER.debug(response_data)
    account = GeoRideUser.from_json(response_data)
    return account


def get_trackers(token):
    """ get user trackers """
    response = _send_request(
        "GET",
        GEORIDE_API_ENDPOINT_TRACKERS,
        token
    )

    response_data = response.json()
    trackers = []
    for json_tracker in response_data:
        _LOGGER.debug(json_tracker)
        trackers.append(GeoRideTracker.from_json(json_tracker))
    return trackers


def get_tracker_beacons(token, tracker_id):
    """ get user trackers """
    response = _send_request(
        "GET",
        GEORIDE_API_ENDPOINT_TRACKER_BEACON.format(trackerId=str(tracker_id)),
        token
    )

    response_data = response.json()
    trackers_beacons = []
    if response.status_code == 200:
        for json_tracker_beacon in response_data:
            _LOGGER.debug(json_tracker_beacon)
            json_tracker_beacon['linked_tracker_id'] = tracker_id
            trackers_beacons.append(GeoRideTrackerBeacon.from_json(json_tracker_beacon))
    return trackers_beacons


def get_trips(token, tracker_id, from_date, to_date):
    """ return all trips between two dates """
    response = _send_request(
        "GET",
        GEORIDE_API_ENDPOINT_TRIPS.format(trackerId=str(tracker_id)),
        token,
        {'from': from_date, 'to': to_date}
    )

    response_data = response.json()
    trips = []
    if response.status_code == 200:
        for json_trip in response_data:
            trips.append(GeoRideTrackerTrip.from_json(json_trip))
    return trips


def get_positions(token, tracker_id, from_date, to_date):
    """ return positions from dates """
    response = _send_request(
        "GET",
        GEORIDE_API_ENDPOINT_POSITIONS.format(trackerId=str(tracker_id)),
        token,
        {'from': from_date, 'to': to_date}
    )

    response_data = response.json()
    positions = []
    if response.status_code == 200:
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


def _share_a_trip(token, tracker_id, trip_id=None, from_date=None,  # pylint: disable= R0913
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

    response = _send_request(
        "POST",
        GEORIDE_API_ENDPOINT_TRIP_SHARE.format(trackerId=str(tracker_id)),
        token,
        data=encoded_data
    )

    response_data = response.json()
    if response.status_code == 200:
        return GeoRideSharedTrip.from_json(response_data)
    return None


def lock_tracker(token, tracker_id):
    """ used to lock a tracker """
    response = _send_request(
        "POST",
        GEORIDE_API_ENDPOINT_LOCK.format(trackerId=str(tracker_id)),
        token
    )
    if response.status_code != 204:
        return False
    return True


def unlock_tracker(token, tracker_id):
    """ used to unlock a tracker """
    response = _send_request(
        "POST",
        GEORIDE_API_ENDPOINT_UNLOCK.format(trackerId=str(tracker_id)),
        token
    )
    if response.status_code != 204:
        return False
    return True


def toogle_lock_tracker(token, tracker_id):
    """ used to toggle lock a tracker """
    response = _send_request(
        "POST",
        GEORIDE_API_ENDPOINT_TOGGLE_LOCK.format(trackerId=str(tracker_id)),
        token
    )
    response_data = response.json()
    return response_data['locked']


def change_tracker_siren_state(token, tracker_id, state: bool):
    """ used to change siren state """
    endpoint = (GEORIDE_API_ENDPOINT_TRACKER_ALARM_ON.format(trackerId=str(tracker_id))) if state \
        else (GEORIDE_API_ENDPOINT_TRACKER_ALARM_OFF.format(trackerId=str(tracker_id)))
    response = _send_request(
        "POST",
        endpoint,
        token
    )
    if response.status_code != 204:
        return False
    return True


def change_tracker_eco_mode_state(token, tracker_id, state: bool):
    """ used to toggle eco mode state """
    endpoint = (GEORIDE_API_ENDPOINT_TRACKER_ECO_MODE_ON.format(trackerId=str(tracker_id))) if state \
        else (GEORIDE_API_ENDPOINT_TRACKER_ECO_MODE_OFF.format(trackerId=str(tracker_id)))
    response = _send_request(
        "POST",
        endpoint,
        token
    )

    if response.status_code != 204:
        return False
    return True


def add_or_update_maintenance(token, tracker_id, maintenance_json):
    """ used to add or update a maintenance """
    response = _send_request(
        "POST",
        GEORIDE_API_ENDPOINT_TRACKER_MAINTENANCE.format(trackerId=str(tracker_id)),
        token,
        data=maintenance_json
    )

    if response.status_code == 204:
        return True
    return False


def delete_maintenance(token, tracker_id, maintenance_id):
    """ used to add or update a maintenance """
    response = _send_request(
        "DELETE",
        GEORIDE_API_ENDPOINT_TRACKER_DELETE_MAINTENANCE.format(
            trackerId=str(tracker_id),
            maintenanceId=str(maintenance_id)
        ),
        token
    )

    if response.status_code == 204:
        return True
    return False


def get_maintenances_for_tracker(token, tracker_id):
    """ used to retrieve maintenances """
    response = _send_request(
        "GET",
        GEORIDE_API_ENDPOINT_TRACKER_MAINTENANCE.format(trackerId=str(tracker_id)),
        token
    )

    response_data = response.json()
    maintenances = []
    if response.status_code == 200:
        for maintenance in response_data['maintenanceList']:
            maintenances.append(GeoRideMaintenance.from_json(maintenance))
        return maintenances
    else:
        return None


def shutdown_tracker(token, tracker_id):
    """ used to toggle lock a tracker """
    response = _send_request(
        "POST",
        GEORIDE_API_ENDPOINT_SHUTDOWN_TRACKER.format(trackerId=str(tracker_id)),
        token
    )
    response_data = response.json()
    if response.status_code == 200:
        return response_data['locked']
    return None


def _send_request(method, endpoint, token, params=None, data=None):
    headers = {"Authorization": "Bearer " + token, "Content-Type": "application/json"} if token else {
        "Content-Type": "application/json"}
    endpoint_url = GEORIDE_API_HOST + endpoint

    if method == "POST":
        return _SESSION.post(endpoint_url, data=data, headers=headers)
    elif method == "GET":
        return _SESSION.get(endpoint_url, params=params, headers=headers)
    elif method == "DELETE":
        return _SESSION.delete(endpoint_url, headers=headers)


if __name__ == '__main__':
    print("Not a main module")
