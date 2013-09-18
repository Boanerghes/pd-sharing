from google.appengine.ext import ndb

class Station(ndb.Model):
    name= ndb.StringProperty('n')
    latitude = ndb.IntegerProperty('la', indexed=False)
    longitude = ndb.IntegerProperty('lo', indexed=False)
    stalls = ndb.IntegerProperty('st')

class StationState(ndb.Model):
    date = ndb.DateTimeProperty('d', auto_now_add=True)
    bikes = ndb.IntegerProperty('b')
    broken = ndb.IntegerProperty('br')
