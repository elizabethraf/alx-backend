#!/usr/bin/env python3
"""Display  Infer appropriate time zone"""
from flask import request
from babel import dates
from pytz import timezone, UnknownTimeZoneError


def get_timezone():
    """get timezone from URL parameter"""
    timezone_param = request.args.get('timezone')
    if timezone_param:
        # Validate timezone using pytz library
        try:
            timezone(timezone_param)
        except UnknownTimeZoneError:
            pass
        else:
            return timezone_param

    # Try to get timezone from user settings
    # Replace this with your own code to get the user's timezone
    user_timezone = 'Europe/London'
    if user_timezone:
        # Validate timezone using pytz library
        try:
            timezone(user_timezone)
        except UnknownTimeZoneError:
            pass
        else:
            return user_timezone

    # Default to UTC
    return 'UTC'


@dates.timezoneselector
def select_timezone():
    """Display time selector"""
    return get_timezone()
