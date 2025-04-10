"""
California Virtual Campus API

A simple API for the California Virtual Campus platform.

:copyright: (c) 2025 Robert Meli
:license: Apache 2.0, see LICENSE for more details.
"""

from CVC_API import _getCourseContentByID

def getCourseContentByID(id:int):
    return _getCourseContentByID(id)