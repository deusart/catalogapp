# from catalogapp.cappengine import engine
# from catalogapp.cappengine import debug
# from catalogapp.cappengine import templates
# from catalogapp.engine import format
from catalogapp.base import Entity
# from catalogapp.engine import calculations
import datetime

class Catalogs(object):
    def __init__(self, engine):
        self.trace = engine.trace
        self.engine = engine
        url = engine.get_template('catalogs','url')
        self.catalogs = engine.get_response(url)
        catalogs = {}
        for item in  self.catalogs:
            catalogs[item['name']] = item ['id']        
        self.ids = tuple(catalogs.values())
        self.names = catalogs
        self.trace('Entity catalogs created.','System')

    def store(self):
        self.engine.save_json('', self.catalogs, 'catalogs')
    
    def info(self):
        print(self.names)

class Dictionaries(Entity):
    pass