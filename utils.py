from google.appengine.ext import ndb

def city_key(city_name):
    """Constructs a Datastore key for a City entity with city_name."""
    return ndb.Key('City', city_name)

def station_key(city_name, station):
    return ndb.Key('City', city_name, 'Station', station)
