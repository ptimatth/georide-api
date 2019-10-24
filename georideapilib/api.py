"""
Georide api lib
@author Matthieu DUVAL <matthieu@duval-dev.fr>
"""

import urllib3
import json

from objects import GeorideTracker, GeorideAccount, GeorideUser, GeorideTrackerTrip, GeorideTrackerPosition, GeorideSharedTrip

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


def getAuthorisationToken(email, password):
    http = urllib3.PoolManager()
    data = {"email": email,"password": password}
    encoded_data = json.dumps(data).encode('utf-8')
    response = http.request(
        'POST', 
        GEORIDE_API_HOST + GEORIDE_API_ENDPOINT_LOGIN,
        body=encoded_data,
        headers={'Content-Type': 'application/json'})
    response_data = json.loads(response.data.decode('utf-8'))
    account = GeorideAccount.fromJson(response_data)
    return account


def renewToken(token):
    http = urllib3.PoolManager()
    headers = {"Authorization": "Bearer " + token}
    response = http.request(
        'GET', 
        GEORIDE_API_HOST + GEORIDE_API_ENDPOINT_NEW_TOKEN,
        headers=headers)
    response_data = json.loads(response.data.decode('utf-8'))
    newToken = response_data['authToken']
    return newToken


def revokeToken(token):
    http = urllib3.PoolManager()
    headers = {"Authorization": "Bearer " + token}
    response = http.request(
        'POST', 
        GEORIDE_API_HOST + GEORIDE_API_ENDPOINT_LOGOUT,
        headers=headers)
    if response.status == 204:
        return True
    else:
        return False


def getUser(token):
    http = urllib3.PoolManager()
    headers = {"Authorization": "Bearer " + token}
    response = http.request(
        'GET', 
        GEORIDE_API_HOST + GEORIDE_API_ENDPOINT_USER,
        headers=headers)
    response_data = json.loads(response.data.decode('utf-8'))
    account = GeorideUser.fromJson(response_data)
    return account  

def getTrackers(token):
    http = urllib3.PoolManager()
    headers = {"Authorization": "Bearer " + token}
    response = http.request(
        'GET', 
        GEORIDE_API_HOST + GEORIDE_API_ENDPOINT_TRAKERS,
        headers=headers)

    response_data = json.loads(response.data.decode('utf-8'))
    trackers = []
    for json_tracker in response_data:
        trackers.append(GeorideTracker.fromJson(json_tracker))
    return trackers


def getTrips(token, trackerId, fromDate, toDate):
    http = urllib3.PoolManager()
    headers = {"Authorization": "Bearer " + token}
    response = http.request(
        'GET', 
        GEORIDE_API_HOST + GEORIDE_API_ENDPOINT_TRIPS.replace(':trackerId', str(trackerId)),
        fields={'from': fromDate, 'to': toDate},
        headers=headers)

    response_data = json.loads(response.data.decode('utf-8'))
    trips = []
    for json_trip in response_data:
        trips.append(GeorideTrackerTrip.fromJson(json_trip))
    return trips

def getPositions(token, trackerId, fromDate, toDate):
    http = urllib3.PoolManager()
    headers = {"Authorization": "Bearer " + token}
    response = http.request(
        'GET', 
        GEORIDE_API_HOST + GEORIDE_API_ENDPOINT_POSITIONS.replace(':trackerId', str(trackerId)),
        fields={'from': fromDate, 'to': toDate},
        headers=headers)

    response_data = json.loads(response.data.decode('utf-8'))
    positions = []
    for json_position in response_data:
        positions.append(GeorideTrackerPosition.fromJson(json_position))
    return positions

def shareATripByTripId(token, trackerId, tripId):
    return _shareATrip(token, trackerId, tripId=tripId)

def shareATripByDate(token, trackerId, fromDate, toDate):
    return _shareATrip(token, trackerId, fromDate=fromDate, toDate=toDate)

def shareATripByTripMergeId(token, trackerId, tripMergedId):
    return _shareATrip(token, trackerId, tripMergedId=tripMergedId)

def _shareATrip(token, trackerId, tripId=None, fromDate=None, toDate=None, tripMergedId=None):
    data = None
    if tripId != None:
        data = {"tripId": tripId}
    elif fromDate != None and toDate != None:
        data = {"from": fromDate, "to": toDate}
    elif tripMergedId != None:
        data = {"tripMergedId": tripMergedId}

    encoded_data = json.dumps(data).encode('utf-8')
    print("Trip data: ", encoded_data)

    http = urllib3.PoolManager()
    headers = {
        "Authorization": "Bearer " + token,
        'Content-Type': 'application/json'
    }
    response = http.request(
        'POST', 
        GEORIDE_API_HOST + GEORIDE_API_ENDPOINT_TRIP_SHARE.replace(':trackerId', str(trackerId)),
        body=encoded_data,
        headers=headers)

    response_data = json.loads(response.data.decode('utf-8'))
    print("Trip data: ", response_data)
    return GeorideSharedTrip.fromJson(response_data)

def lockTracker(token, trackerId):
    http = urllib3.PoolManager()
    headers = {"Authorization": "Bearer " + token}
    response = http.request(
        'POST', 
        GEORIDE_API_HOST + GEORIDE_API_ENDPOINT_LOCK.replace(':trackerId', str(trackerId)),
        headers=headers)
    if response.status == 204:
        return True
    else:
        return False

def unlockTracker(token, trackerId):
    http = urllib3.PoolManager()
    headers = {"Authorization": "Bearer " + token}
    response = http.request(
        'POST', 
        GEORIDE_API_HOST + GEORIDE_API_ENDPOINT_UNCLOCK.replace(':trackerId', str(trackerId)),
        headers=headers)
    if response.status == 204:
        return True
    else:
        return False

def toogleLockTracker(token, trackerId):
    http = urllib3.PoolManager()
    headers = {"Authorization": "Bearer " + token}
    response = http.request(
        'POST', 
        GEORIDE_API_HOST + GEORIDE_API_ENDPOINT_TOGGLE_LOCK.replace(':trackerId', str(trackerId)),
        headers=headers)
    response_data = json.loads(response.data.decode('utf-8'))
    return response_data['locked']

if __name__ == '__main__':
    print("Not a main module")

