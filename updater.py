import webapp2
import lib.gb
import utils

from db_schema import Station, StationState

from google.appengine.ext import ndb

class Updater(webapp2.RequestHandler):

    def get(self):

        #for debugging only
        self.response.headers['Content-Type'] = 'text/plain'

        # fetch stations from official site
        stations  = lib.gb.get_all()

        #iterate and update
        for s in stations:
            k = utils.station_key("Padova", str(s.idx))
            obj = StationState.query(ancestor=k).order(-StationState.date).fetch(1)[0]

            if int(obj.bikes) != int(s.bikes) or int(obj.broken) != s.broken:
                #self.response.write('updated ' + str(k) + ' ' + str(obj.bikes) + ' to ' + str(s.bikes) + '\n')
                StationState(parent= k, bikes=s.bikes, broken=s.broken).put()


application = webapp2.WSGIApplication([
    ('/tasks/update', Updater),
], debug=True)


# obj = Station.get_or_insert(
#                 str(s.idx), 
#                 parent= utils.city_key('Padova'), 
#                 name=str(s.name), 
#                 latitude=s.lat,
#                 longitude=s.lat,
#                 stalls=s.bikes + s.free, 
#                 bikes=-1)
