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
            obj = Station.get_or_insert(
                str(s.idx), 
                parent= utils.city_key('Padova'), 
                name=str(s.name), 
                latitude=s.lat,
                longitude=s.lat,
                stalls=s.bikes + s.free, 
                bikes=-1)

            if str(obj.bikes) != str(s.bikes):
                self.response.write('updated ' + obj.name + ' ' + str(obj.bikes) + ' to ' + str(s.bikes) + '\n')

                StationState(parent= obj.key, bikes=s.bikes).put()
                # update redundant property
                obj.bikes = s.bikes
                obj.put()

application = webapp2.WSGIApplication([
    ('/tasks/update', Updater),
], debug=True)
