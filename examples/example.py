import api as GeorideApi
from objects import GeorideAccount

import datetime
import time


""" If ypu out to reuse account """
"""
account = GeorideAccount(<your_id>, <yout_email>, <is_admin>, <your_token>)
"""

""" Get an acces token """
account = GeorideApi.getAuthorisationToken("<your_email>", "<your_passord>")
print("token 1: ", account.authToken)


""" do not abuse, renew when previous token have almost reached time """
"""
account.authToken = GeorideApi.renewToken(account.authToken)
print("token 2: ", account.authToken)
"""

user = GeorideApi.getUser(account.authToken)
print("User: ", user.firstName)

trackers = GeorideApi.getTrackers(account.authToken)
tracker = trackers[0]
print("Tracker name: ", tracker.trackerName)

trips = GeorideApi.getTrips(account.authToken, tracker.trackerId, "2019-10-10", "2019-10-24")
trip = trips[0];
trip_date = datetime.datetime.strptime("2019-10-10T06:45:34.000Z", '%Y-%m-%dT%H:%M:%S.%fZ')
print("Trip date: {}, from: {}, to: {}".format(trip_date, trip.niceStartAddress, trip.niceEndAddress))

positions = GeorideApi.getPositions(account.authToken, tracker.trackerId, "2019-10-10", "2019-10-24")
position = positions[0];
print("Position speed: {}, lon: {}, lat: {}".format(position.speed, position.longitude, position.latitude))


tripShared = GeorideApi.shareATripByDate(account.authToken, tracker.trackerId, fromDate="2019-10-10", toDate="2019-10-24")
print("tripShared url: {}, id: {}".format(tripShared.url, tripShared.shareId))

time.sleep(30)
haveBeenLocked = GeorideApi.lockTracker(account.authToken, tracker.trackerId)
print("Tracker have been locked: ", haveBeenLocked)

time.sleep(30)
haveBeenUnlocked = GeorideApi.lockTracker(account.authToken, tracker.trackerId)
print("Tracker have been unlocked: ", haveBeenUnlocked)

time.sleep(30)
isLocked = GeorideApi.toogleLockTracker(account.authToken, tracker.trackerId)
print("Tracker is locked: ", haveBeenUnlocked)

time.sleep(30)
trackers = GeorideApi.getTrackers(account.authToken)
tracker = trackers[0]
print("Tracker name: ", tracker.trackerName, " is locked: ", tracker.isLocked)

"""
GeorideApi.revokeToken(account.authToken)
"""