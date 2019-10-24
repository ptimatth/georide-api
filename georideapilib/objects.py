"""
Georide objects implementation
@author Matthieu DUVAL <matthieu@duval-dev.fr>
"""

class GeorideSharedTrip:
	def __init__(self, url, shareId):
		self._url = url
		self._shareId = shareId

	@property
	def url(self):
		return self._url
	
	@property
	def shareId(self):
		return self._shareId

	def fromJson(json):
		return GeorideSharedTrip(
				json['url'],
				json['shareId']
			)

class GeorideTrackerTrip:
	def __init__(self, tripId, trackerId, averageSpeed, maxSpeed, distance, duration, startAddress, niceStartAddress, startLat,
	 startLon, endAddress, niceEndAddress, endLat, endLon, startTime, endTime):
		self._tripId = tripId
		self._trackerId = trackerId
		self._averageSpeed = averageSpeed
		self._maxSpeed = maxSpeed
		self._distance = distance
		self._duration = duration
		self._startAddress = startAddress
		self._niceStartAddress = niceStartAddress
		self._startLat = startLat
		self._startLon = startLon
		self._endAddress = endAddress
		self._niceEndAddress = niceEndAddress
		self._endLat = endLat
		self._endLon = endLon
		self._startTime = startTime
		self._endTime = endTime
	
	@property
	def tripId(self):
		return self._tripId
	
	@property
	def trackerId(self):
		return self._trackerId
	
	@property
	def averageSpeed(self):
		return self._averageSpeed
	
	@property
	def maxSpeed(self):
		return self._maxSpeed
	
	@property
	def distance(self):
		return self._distance
	
	@property
	def duration(self):
		return self._duration
	
	@property
	def startAddress(self):
		return self._startAddress
	
	@property
	def niceStartAddress(self):
		return self._niceStartAddress
	
	@property
	def startLat(self):
		return self._startLat
	
	@property
	def startLon(self):
		return self._startLon
	
	@property
	def endAddress(self):
		return self._endAddress
	
	@property
	def niceEndAddress(self):
		return self._niceEndAddress
	
	@property
	def endLat(self):
		return self._endLat
	
	@property
	def endLon(self):
		return self._endLon
	
	@property
	def startTime(self):
		return self._startTime
	
	@property
	def endTime(self):
		return self._endTime

	def fromJson(json):
		return GeorideTrackerTrip(
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


class GeorideTrackerPosition:
	def __init__(self, fixtime, latitude, longitude, altitude, speed, address):
		self._fixtime = fixtime
		self._latitude = latitude
		self._longitude = longitude
		self._altitude = altitude
		self._speed = speed
		self._address = address

	@property
	def fixtime(self):
		return self._fixtime

	@property
	def latitude(self):
		return self._latitude

	@property
	def longitude(self):
		return self._longitude

	@property
	def altitude(self):
		return self._altitude

	@property
	def speed(self):
		return self._speed

	@property
	def address(self):
		return self._address

	def fromJson(json):
		return GeorideTrackerPosition(
				json['fixtime'],
				json['latitude'],
				json['longitude'],
				json['altitude'],
				json['speed'],
				json['address']
			)




class GeorideTracker:
	def __init__(self, trackerId, trackerName, deviceButtonAction, deviceButtonDelay, vibrationLevel, isOldTracker, autoLockFreezedTo, 
			fixtime, role, lastPaymentDate, giftCardId, expires, activationDate, odometer, isStolen, isCrashed,	crashDetectionDisabled,
			speed, moving, positionId,  latitude, longitude, altitude, lockedPositionId, lockedLatitude, lockedLongitude, isLocked,
			canSeePosition, canLock, canUnlock, canShare, canUnshare, canCheckSpeed, canSeeStatistics, canSendBrokenDownSignal,
			canSendStolenSignal, status):
		self._trackerId =				trackerId
		self._trackerName =				trackerName
		self._deviceButtonAction =		deviceButtonAction
		self._deviceButtonDelay =		deviceButtonDelay
		self._vibrationLevel =			vibrationLevel
		self._isOldTracker =			isOldTracker
		self._autoLockFreezedTo =		autoLockFreezedTo
		self._fixtime =					fixtime
		self._role =					role
		self._lastPaymentDate =			lastPaymentDate
		self._giftCardId =				giftCardId
		self._expires =					expires
		self._activationDate =			activationDate
		self._odometer =				odometer
		self._isStolen =				isStolen
		self._isCrashed =				isCrashed
		self._crashDetectionDisabled =	crashDetectionDisabled
		self._speed =					speed
		self._moving =					moving
		self._positionId =				positionId
		self._latitude =				latitude
		self._longitude =				longitude
		self._altitude =				altitude
		self._lockedPositionId =		lockedPositionId
		self._lockedLatitude =			lockedLatitude
		self._lockedLongitude =			lockedLongitude
		self._isLocked =				isLocked
		self._canSeePosition =			canSeePosition
		self._canLock =					canLock
		self._canUnlock =				canUnlock
		self._canShare =				canShare
		self._canUnshare =				canUnshare
		self._canCheckSpeed =			canCheckSpeed
		self._canSeeStatistics =		canSeeStatistics
		self._canSendBrokenDownSignal =	canSendBrokenDownSignal
		self._canSendStolenSignal =		canSendStolenSignal
		self._status = 					status

	@property
	def trackerId(self):
		return self._trackerId

	@property
	def trackerName(self):
		return self._trackerName

	@property
	def deviceButtonAction(self):
		return self._deviceButtonAction
	
	@property
	def deviceButtonDelay(self):
		return self._deviceButtonDelay
	
	@property
	def vibrationLevel(self):
		return self._vibrationLevel
	
	@property
	def isOldTracker(self):
		return self._isOldTracker
	
	@property
	def autoLockFreesedTo(self):
		return self._autoLockFreesedTo

	@property
	def fixtime(self):
		return self._fixtime
	
	@property
	def role(self):
		return self._role
	
	@property
	def lastPayementDate(self):
		return self._lastPayementDate
	
	@property
	def giftCardId(self):
		return self._giftCardId
	
	@property
	def expires(self):
		return self._expires

	@property
	def activationDate(self):
		return self._activationDate

	@property
	def odometer(self):
		return self._odometer

	@property
	def isStolen(self):
		return self._isStolen

	@property
	def isCrashed(self):
		return self._isCrashed

	@property
	def crashDetectionDisabled(self):
		return self._crashDetectionDisabled

	@property
	def speed(self):
		return self._speed

	@property
	def moving(self):
		return self._moving

	@property
	def positionId(self):
		return self._positionId

	@property
	def latitude(self):
		return self._latitude

	@property
	def longitude(self):
		return self._longitude

	@property
	def altitude(self):
		return self._altitude

	@property
	def lockedPositionId(self):
		return self._lockedPositionId

	@property
	def lockedLatitude(self):
		return self._lockedLatitude

	@property
	def lockedLongitude(self):
		return self._lockedLongitude

	@property
	def isLocked(self):
		return self._isLocked

	@property
	def canSeePosition(self):
		return self._canSeePosition

	@property
	def canLock(self):
		return self._canLock

	@property
	def canUnlock(self):
		return self._canUnlock

	@property
	def canShare(self):
		return self._canShare

	@property
	def canUnshare(self):
		return self._canUnshare

	@property
	def canCheckSpeed(self):
		return self._canCheckSpeed

	@property
	def canSeeStatistics(self):
		return self._canSeeStatistics

	@property
	def canSendBrokenDownSignal(self):
		return self._canSendBrokenDownSignal

	@property
	def canSendStolenSignal(self):
		return self._canSendStolenSignal

	@property
	def status(self):
		return self._status

	def fromJson(json):
		return GeorideTracker(
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


class GeorideAccount:
	def __init__(self, account_id, email, isAdmin, authToken):
		self._account_id = account_id
		self._email = email
		self._isAdmin = isAdmin
		self._authToken = authToken

	@property
	def account_id(self):
		return self._account_id

	@property
	def email(self):
		return self._email

	@property
	def isAdmin(self):
		return self._isAdmin

	@property
	def authToken(self):
		return self._authToken

	@authToken.setter
	def authToken(self, newToken):
		self._authToken = newToken

	def fromJson(json):
		return GeorideAccount(
	        json['id'],
	        json['email'],
	        json['isAdmin'],
	        json['authToken']
        )


class GeorideUser:
	def __init__(self, account_id, email, firstName, createdAt,	phoneNumberp, pushUserToken, legal,	dateOfBirth):
		self._account_id = account_id
		self._email = email
		self._firstName = firstName
		self._createdAt = createdAt
		self._phoneNumberp = phoneNumberp
		self._pushUserToken = pushUserToken
		self._legal = legal
		self._dateOfBirth = dateOfBirth

	@property
	def user_id(self):
		return self._user_id

	@property
	def email(self):
		return self._email

	@property
	def firstName(self):
		return self._firstName

	@property
	def createdAt(self):
		return self._createdAt
	
	@property
	def phoneNumber(self):
		return self._phoneNumber
	
	@property
	def pushUserToken(self):
		return self._pushUserToken
	
	@property
	def legal(self):
		return self._legal

	@property
	def dateOfBirth(self):
		return self._dateOfBirth

	def fromJson(json):
		return GeorideUser(
	        json['id'],
	        json['email'],
	        json['firstName'],
	        json['createdAt'],
	        json['phoneNumber'],
	        json['pushUserToken'],
	        json['legal'],
	        json['dateOfBirth']
        )



if __name__ == '__main__':
    print("Not a main module")