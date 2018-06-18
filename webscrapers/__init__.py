"""
A module with a common API for all web scrapers / crawlers for rental
data acquisition from popular sites.
"""

from wggesuchtde import WGGesuchtDE
from location import Location
from api import DATADIR


__all__ = ["WGGesuchtDE", "Location", "DATADIR"]
