""" all GeoRide exception """

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class LoginException(Error):
    """loggin exception"""
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class UnauthorizedException(Error):
    """loggin exception"""
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class SeverException(Error):
    """loggin exception"""
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
