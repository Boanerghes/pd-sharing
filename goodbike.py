import webapp2
import lib.gb
import utils

from db_schema import Station, StationState

from google.appengine.ext import ndb

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'

        # delst = Station.query()
        # for d in delst:
        #     d.key.delete()

        # delstsit = StationState.query()
        # for d in delstsit:
        #     d.key.delete()

        st = Station.query(ancestor=utils.city_key('Padova')).fetch(50)

        for g in st:
            self.response.write(g.name + ' ' + str(g.bikes) + '/' + str(g.stalls) + '\n')

            ris = StationState.query(ancestor=g.key).order(StationState.date).fetch(10)
            for r in ris:
                self.response.write(str(r.date) + ' ' + str(r.bikes) + '\n')

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

def city_key(city_name):
    """Constructs a Datastore key for a City entity with city_name."""
    return ndb.Key('City', city_name)
