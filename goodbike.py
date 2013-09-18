import webapp2
import lib.gb
import utils

from db_schema import Station, StationState

from google.appengine.ext import ndb

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'

        st = Station.query(ancestor=utils.city_key('Padova')).fetch(50)

        for g in st:
            k = utils.station_key("Padova", str(g.key.id()))
            sit = StationState.query(ancestor=k).order(-StationState.date).fetch(1)[0]

            self.response.write(g.name + ' ' + str(sit.bikes) + '/' + str(g.stalls) + ' -' + str(sit.broken) + '\n')
            ris = StationState.query(ancestor=g.key).order(-StationState.date).fetch(10)
            for r in ris:
                self.response.write(str(r.date) + ' ' + str(r.bikes) + '\n')

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

def city_key(city_name):
    """Constructs a Datastore key for a City entity with city_name."""
    return ndb.Key('City', city_name)
